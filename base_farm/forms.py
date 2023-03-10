from django.forms import ModelForm
from .models import FarmRegister, Farm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class FarmRegisterForm(ModelForm):
    class Meta:
        model = FarmRegister
        fields = '__all__'


class FarmForm(ModelForm):
    class Meta:
        model = Farm
        fields = ['name', 'description', 'size', 'location', 'is_mine']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EndUserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'