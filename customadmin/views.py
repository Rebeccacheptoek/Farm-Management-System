from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Crop, Farm

from .forms import CropForm, FarmForm, UserForm


# Create your views here.
def admin_login(request):
    # response = HttpResponseRedirect("Hello backend world")
    # return render(request, 'lologingin.html')
    try:
        if request.user.is_authenticated:
            return redirect('back-home')
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.info(request, 'Account not found')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            user_obj = authenticate(username=username, password=password)

            if user_obj and user_obj.is_superuser:
                login(request, user_obj)
                return redirect('back-home')

            messages.info(request, 'Invalid password')
            return redirect('/')
        return render(request, 'login.html')
    except Exception as e:
        print(e)


@login_required(login_url='custom-login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('backend-home')
    context = {'form': form}
    return render(request, 'update_user.html', context)


def index(request):
    return render(request, 'index.html')


def crop(request):
    crops = Crop.objects.all()
    context = {'crops': crops}
    return render(request, 'crop.html', context)


@login_required(login_url='custom-login')
def generateReport(request):
    return render(request, 'generate_report.html')


def farm(request):
    farms = Farm.objects.all()
    context = {'farms': farms}
    return render(request, 'farm.html', context)


@login_required(login_url='custom-login')
def createFarm(request):
    form = FarmForm()
    if request.method == 'POST':
        form = FarmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farm')
    context = {'form': form}
    return render(request, 'create_farm.html', context)


@login_required(login_url='custom-login')
def updateFarm(request, pk):
    farm = Farm.objects.get(id=pk)
    form = FarmForm(instance=farm)
    if request.method == 'POST':
        form = FarmForm(request.POST, instance=farm)
        if form.is_valid():
            form.save()
            return redirect('farm')

    context = {'form': form}
    return render(request, 'create_farm.html', context)


@login_required(login_url='custom-login')
def updateCrop(request, pk):
    crop = Crop.objects.get(id=pk)
    form = CropForm(instance=crop)
    if request.method == 'POST':
        form = CropForm(request.POST, instance=crop)
        if form.is_valid():
            form.save()
            return redirect('crop')

    context = {'form': form}
    return render(request, 'add_crop.html', context)


@login_required(login_url='custom-login')
def addCrop(request):
    form = CropForm()
    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('b-crop')
    context = {'form': form}
    return render(request, 'add_crop.html', context)


@login_required(login_url='custom-login')
def delete(request, pk):
    farm = Farm.objects.get(id=pk)
    if request.method == 'POST':
        farm.delete()
        return redirect('farm')
    return render(request, 'delete.html', {'obj': farm})
