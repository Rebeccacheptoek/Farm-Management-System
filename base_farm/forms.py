from django.forms import ModelForm
from .models import FarmRegister, Farm


class FarmRegisterForm(ModelForm):
    class Meta:
        model = FarmRegister
        fields = '__all__'


class FarmForm(ModelForm):
    class Meta:
        model = Farm
        fields = '__all__'
