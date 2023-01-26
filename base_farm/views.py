from django.shortcuts import render, redirect
from .models import Farm, Crop, FarmRegister, Category, FarmCrop, FarmLease, FarmNotes
from .forms import FarmRegisterForm, FarmForm

# from django.contrib.auth.forms import us

farms = [
    {'id': 1, 'name': 'Kitale home farm', 'location': 'Kitale', 'size': 2, 'is_mine': True},
    {'id': 2, 'name': 'Eldoret home farm', 'location': 'Eldoret', 'size': 5, 'is_mine': True},
    {'id': 3, 'name': 'Kinyoro maize farm', 'location': 'Kinyoro', 'size': 12, 'is_mine': False}
]


def home(request):
    farms = Farm.objects.all()
    context = {'farms': farms}
    return render(request, 'base_farm/home.html', context)


def farm(request, pk):
    farm_ = Farm.objects.get(id=pk)
    context = {'farm': farm}
    return render(request, 'base_farm/farm.html', context)


def createFarm(request):
    form = FarmForm()
    if request.method == 'POST':
        form = FarmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base_farm/farm_form.html')


def crop(request):
    crop = Crop.objects.all()
    return render(request, 'base_farm/crop.html')


def farmRegister(request):
    # farm_register = FarmRegister.objects.all()
    form = FarmRegisterForm()
    if request.method == 'POST':
        form = FarmRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base_farm/farm_register_form.html', context)
