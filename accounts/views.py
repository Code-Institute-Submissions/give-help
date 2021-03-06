from django.shortcuts import redirect, reverse, render
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from home.views import index
from accounts.forms import UserLoginForm, UserRegistrationForm, EditProfileForm, DonorForm
from django.contrib.auth.models import User
from accounts.models import Donor
from django.db.models.signals import post_save
from django.dispatch import receiver
from subscribe.forms import EmailSignupForm

# Create your views here.


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "Successfully logged out")
    return redirect(reverse('index'))


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    subscribe_form = EmailSignupForm()

    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Successfully logged in!")
                return redirect(reverse('index'))
            else:
                login_form = UserLoginForm()
                messages.error(request, "Username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form, 'subscribe_form': subscribe_form})


def registration(request):
    if request.user.is_authenticated:
        messages.error(request, "You are already logged in")
        return redirect(reverse('index'))

    subscribe_form = EmailSignupForm()

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            messages.success(request, "Your account has been created")

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                messages.error(
                    request, "Something went wrong, please try again")
    else:
        registration_form = UserRegistrationForm()

    return render(request, 'registration.html', {"registration_form": registration_form, 'subscribe_form': subscribe_form})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Donor.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


def view_profile(request):
    donor = Donor.objects.get(user_id=request.user.id)
    subscribe_form = EmailSignupForm()
    return render(request, 'profile.html', {"donor": donor, 'subscribe_form': subscribe_form})


def edit_profile(request):
    subscribe_form = EmailSignupForm()

    if request.method == "POST":
        edit_profile_form = EditProfileForm(
            request.POST, instance=request.user)
        edit_donor_form = DonorForm(
            request.POST, instance=request.user.profile)

        if edit_profile_form.is_valid() and edit_donor_form.is_valid():
            edit_profile_form.save()
            edit_donor_form.save()
            messages.success(request, "Account updated")
            return redirect('view_profile')
        else:
            messages.error(request, ('Please correct the error'))
    else:
        edit_profile_form = EditProfileForm(instance=request.user)
        edit_donor_form = DonorForm(instance=request.user.profile)
        return render(request, 'edit-profile.html', {"edit_profile_form": edit_profile_form, 'edit_donor_form': edit_donor_form, 'subscribe_form': subscribe_form})
