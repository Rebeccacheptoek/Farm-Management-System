from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Farm, Crop, FarmRegister, Category, FarmCrop, FarmLease, FarmNotes
from .forms import FarmRegisterForm, FarmForm, CreateUserForm, EndUserForm
from django.contrib.auth.forms import UserCreationForm

# from django.contrib.auth.forms import us

farms = [
    {'id': 1, 'name': 'Kitale home farm', 'location': 'Kitale', 'size': 2, 'is_mine': True},
    {'id': 2, 'name': 'Eldoret home farm', 'location': 'Eldoret', 'size': 5, 'is_mine': True},
    {'id': 3, 'name': 'Kinyoro maize farm', 'location': 'Kinyoro', 'size': 12, 'is_mine': False}
]


def registerUser(request):
    # form = UserCreationForm()
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('login')
        else:
            messages.error(request, 'An error occurred during registration')
    return render(request, 'base_farm/register.html', {'form': form})


# def registerPage(request):
#     form = CreateUserForm()
#
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request, 'Account created successfully for ' + user)
#
#             return redirect('login')
#
#     context = {'form': form}
#     return render(request, 'base_farm/register.html', context)


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist')

    context = {'page': page}
    return render(request, 'base_farm/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def endUser(request):
    form = EndUserForm()
    if request.method == 'POST':
        form = EndUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return redirect('home', context)
# def loginPage(request):
#     context = {}
#     return render(request, 'base_farm/login.html', context)


def home(request):
    farms = Farm.objects.all()
    categories = Category.objects.all()
    registered_farms = FarmRegister.objects.all()
    context = {'farms': farms, 'categories': categories, 'registered_farms': registered_farms}
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
    return render(request, 'base_farm/farm_form.html', context)


def updateFarm(request, pk):
    farm = Farm.objects.get(id=pk)
    form = FarmForm(instance=farm)
    if request.method == 'POST':
        form = FarmForm(request.POST, instance=farm)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base_farm/farm_form.html', context)


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


def deleteFarm(request, pk):
    farm = Farm.objects.get(id=pk)
    if request.method == 'POST':
        farm.delete()
        return redirect('home')
    return render(request, 'base_farm/delete.html', {'obj': farm})
