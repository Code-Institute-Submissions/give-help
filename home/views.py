from django.shortcuts import render
from subscribe.forms import EmailSignupForm
from .models import Galerry


def index(request):
    features = '<section class="section"> <div class="row"> <div class="col s12 l6 main-heading"> <div class="features-left"> <h6 class="left-align">What they have now:</h6> <p class="grey-text text-darken-2"><i class="material-icons">sentiment_very_dissatisfied</i>One Pediatric Oncology department with 31 beds</p><p class="grey-text text-darken-2"><i class="material-icons">sentiment_very_dissatisfied</i>Shared bathrooms</p><p class="grey-text text-darken-2"><i class="material-icons">sentiment_very_dissatisfied</i>The department is on the same floor as an ENT department</p><p class="grey-text text-darken-2"><i class="material-icons">sentiment_very_dissatisfied</i>The General Surgery department also handles children with cancer</p><p class="grey-text text-darken-2"><i class="material-icons">sentiment_very_dissatisfied</i>The Intensive Care department also treats oncological patients</p><p class="grey-text text-darken-2"><i class="material-icons">sentiment_very_dissatisfied</i>No medical protocols and no multidisciplinary approach</p></div></div><div class="col s12 l6 main-heading"> <div class="features-right"> <h6 class="left-align">What investment bring:</h6> <p class="grey-text text-darken-2"><i class="material-icons">sentiment_very_satisfied</i>Radiotherapy - two bunkers on the basement floor and the patient prep spaces</p><p class="grey-text text-darken-2"><i class="material-icons">sentiment_very_satisfied</i>An Oncology department - day admission and continuous admission</p><p class="grey-text text-darken-2"><i class="material-icons">sentiment_very_satisfied</i>A Hemato-Oncology department, with wards and 5 sterile rooms</p><p class="grey-text text-darken-2"><i class="material-icons">sentiment_very_satisfied</i>Space for a new MRI and a new CT with enough anesthetize rooms</p><p class="grey-text text-darken-2"><i class="material-icons">sentiment_very_satisfied</i>A surgical department and a neurosurgical department</p></div></div></div></section>'
    subscribe_form = EmailSignupForm()
    return render(request, "index.html", {'features': features, 'subscribe_form': subscribe_form})


def gallery(request):
    images = Galerry.objects.all()
    subscribe_form = EmailSignupForm()
    return render(request, "gallery.html", {'images': images, 'subscribe_form': subscribe_form})