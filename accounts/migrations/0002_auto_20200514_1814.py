# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-14 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
    ]
