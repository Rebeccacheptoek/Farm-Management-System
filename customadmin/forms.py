from django.forms import ModelForm
from .models import Crop, Farm, Category, FarmCrop, FarmLease, FarmNotes, FarmRegister
from django import forms
from django.contrib.auth.models import User


class CropForm(ModelForm):
    class Meta:
        model = Crop
        fields = '__all__'



# class FarmForm(ModelForm):
#     class Meta:
#         model = Farm
#         fields = ['name', 'description', 'size', 'location', 'is_mine']
class FarmForm(ModelForm):
    class Meta:
        model = Farm
        fields = ['name', 'description', 'size', 'location', 'is_mine']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'parent_category']


class FarmRegisterForm(ModelForm):
    class Meta:
        model = FarmRegister
        fields = ['farm_crop_id', 'category_id', 'unit_cost', 'unit_acre', 'total_cost', 'quantity', 'description']


class FarmNoteForm(ModelForm):
    class Meta:
        model = FarmNotes
        fields = '__all__'


class FarmCropForm(ModelForm):
    class Meta:
        model = FarmCrop
        fields = '__all__'


class FarmLeaseForm(ModelForm):
    class Meta:
        model = FarmLease
        fields = '__all__'
