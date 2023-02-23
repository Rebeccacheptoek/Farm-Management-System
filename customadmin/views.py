from django.contrib import messages
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Crop, Farm, FarmRegister, FarmCrop, FarmLease, FarmNotes, Category
# from slick_reporting.views import SlickReportView
# from slick_reporting.fields import SlickReportField
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


def crop(request):
    crops = Crop.objects.all()
    context = {'crops': crops}
    return render(request, 'crop.html', context)


def viewCrop(request, pk):
    crops = Crop.objects.get(id=pk)
    farm_crop = FarmCrop.objects.all()
    context = {'crops': crops, 'farm_crop': farm_crop}
    return render(request, 'view-crop.html', context)


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
def updateCrop(request, pk):
    crop = Crop.objects.get(id=pk)
    form = CropForm(instance=crop)
    if request.method == 'POST':
        form = CropForm(request.POST, instance=crop)
        if form.is_valid():
            form.save()
            return redirect('b-crop')

    context = {'form': form}
    return render(request, 'add_crop.html', context)


def category(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'category.html', context)


def farmLease(request):
    farm_leases = FarmLease.objects.all()
    context = {'farm_leases': farm_leases}
    return render(request, 'farm_lease.html', context)


def farmCrop(request):
    farm_crops = FarmCrop.objects.all()
    context = {'farm_crops': farm_crops}
    return render(request, 'farm_crop.html', context)


def farmNote(request):
    farm_notes = FarmNotes.objects.all()
    context = {'farm_notes': farm_notes}
    return render(request, 'farm_notes.html', context)

@login_required(login_url='custom-login')
def delete(request, pk):
    farm = Farm.objects.get(id=pk)
    if request.method == 'POST':
        farm.delete()
        return redirect('farm')
    return render(request, 'delete.html', {'obj': farm})


# @login_required(login_url='custom-login')
# def generateReport(request):
#     return render(request, 'generate_report.html')


# def TotalFarmExpenses(SlickReportView):
#     report_model = FarmRegister
#     date_field = 'date_created'
#     group_by = 'farm_crop_id'
#     columns = ['title',
#                SlickReportField.create(method=Sum, field='total_cost', name='total__cost', verbose_name='Total spent $')
#                ]
#
#     # Charts
#     charts_settings = [
#         {
#             'type': 'bar',
#             'data_source': 'total__cost',
#             'title_source': 'title',
#         },
#     ]
#     return render(SlickReportView, 'generate_report.html')
