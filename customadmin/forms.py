from django.forms import ModelForm
from .models import Crop
from django import forms
from django.contrib.auth.models import User


class CropForm(ModelForm):
    class Meta:
        model = Crop
        fields = ['name', 'description', 'duration']
