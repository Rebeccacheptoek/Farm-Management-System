from django.forms import ModelForm
from .models import Crop, Farm
from django import forms
from django.contrib.auth.models import User


class CropForm(ModelForm):
    class Meta:
        model = Crop
        fields = ['name', 'description', 'duration']


class FarmForm(ModelForm):
    class Meta:
        model = Farm
        fields = ['name', 'description', 'size', 'location', 'is_mine']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']