from django.contrib import messages
from django.db.models import Sum
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Crop, Farm, FarmRegister, FarmCrop, FarmLease, FarmNotes, Category
# from slick_reporting.views import SlickReportView
# from slick_reporting.fields import SlickReportField
from .forms import *
# from .forms import CategoryForm, FarmRegisterForm, FarmNoteForm, FarmCropForm
from django.views.generic import TemplateView

import pdb


# Create your views here.
def admin_login(request):
    # response = HttpResponseRedirect("Hello backend world")
    # return render(request, 'lologingin.html')
    try:
        if request.user.is_authenticated:
            return redirect('backend-home')
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
                return redirect('backend-home')

            messages.info(request, 'Invalid password')
            return redirect('/')
        return render(request, 'admin/login.html')
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
    form = FarmForm()
    if request.method == 'POST':
        form = FarmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farm')
    context = {'farms': farms, 'form': form}
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
    farm_crop = FarmCrop.objects.all()
    form = CropForm()
    if request.method == 'POST':
        form = CropForm(request.POST)
        # import pdb
        # pdb.set_trace()
        if form.is_valid():
            form.save()
            return redirect('b-crop')
        else:
            # Handle invalid form data here, e.g.:
            return HttpResponse('Invalid form data')
            pass
    context = {'crops': crops, 'form': form, 'farm_crop': farm_crop}
    return render(request, 'crop.html', context)


def viewCrop(request, pk):
    crops = Crop.objects.get(id=pk)
    farm_crop = FarmCrop.objects.all()
    context = {'crops': crops, 'farm_crop': farm_crop}
    return render(request, 'view-crop.html', context)


# @login_required(login_url='custom-login')
# def addCrop(request):
#     form = CropForm()
#     if request.method == 'POST':
#         form = CropForm(request.POST)
#         # import pdb
#         # pdb.set_trace()
#         if form.is_valid():
#             form.save()
#             return redirect('b-crop')
#         else:
#             # Handle invalid form data here, e.g.:
#             return HttpResponse('Invalid form data')
#             pass
#     context = {'form': form}
#     return render(request, 'add_crop.html', context)


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
    categories = Category.objects.all()
    parents = Category.objects.filter(parent_category_id=None)
    form = CategoryForm()
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        parent_category_id = request.POST['parent_category_id']

        Category.objects.create(name=name, description=description, parent_category_id=parent_category_id)
        # name = request.POST['name']
        # form = CategoryForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return redirect('category')
    context = {'categories': categories, 'form': form, 'parents': parents}
    return render(request, 'category.html', context)


# def addCategory(request):
#     parents = Category.objects.filter(parent_category_id=None)
#     form = CategoryForm()
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('category')
#     context = {'form': form, 'parents': parents}
#     return render(request, 'add_category.html', context)


def farmLease(request):
    farm_leases = FarmLease.objects.all()
    form = FarmLeaseForm()
    if request.method == 'POST':
        form = FarmLeaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farm-lease')
    context = {'farm_leases': farm_leases, 'form': form}
    return render(request, 'farm_lease.html', context)


# def addFarmLease(request):
#     form = FarmLeaseForm()
#     if request.method == 'POST':
#         form = FarmLeaseForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('farm-lease')
#     context = {'form': form}
#     return render(request, 'add_farm_lease.html', context)


def farmCrop(request):
    farm_crops = FarmCrop.objects.all()
    form = FarmCropForm()
    if request.method == 'POST':
        form = FarmCropForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farm-crop')
    context = {'farm_crops': farm_crops, 'form': form}
    return render(request, 'farm_crop.html', context)


# def addFarmCrop(request):
#     form = FarmCropForm()
#     if request.method == 'POST':
#         form = FarmCropForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('farm-crop')
#     context = {'form': form}
#     return render(request, 'add_farm_crop.html', context)


def farmNote(request):
    farm_notes = FarmNotes.objects.all()
    form = FarmNoteForm()
    if request.method == 'POST':
        form = FarmNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farm-note')
    context = {'farm_notes': farm_notes, 'form': form}
    return render(request, 'farm_notes.html', context)


# def addFarmNote(request):
#     form = FarmNoteForm()
#     if request.method == 'POST':
#         form = FarmNoteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('farm-note')
#     context = {'form': form}
#     return render(request, 'add_farm_note.html', context)


def farmRegister(request):
    farm_registers = FarmRegister.objects.all()
    form = FarmRegisterForm()
    if request.method == 'POST':
        form = FarmRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farm-register')
        else:
            # Handle invalid form data here, e.g.:
            return HttpResponse('Invalid form data')
            pass
    context = {'farm_registers': farm_registers, 'form': form}
    return render(request, 'farm_register.html', context)


# def addFarmRegister(request):
#     form = FarmRegisterForm()
#     if request.method == 'POST':
#         form = FarmRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('farm-register')
#         else:
#             # Handle invalid form data here, e.g.:
#             return HttpResponse('Invalid form data')
#             pass
#     context = {'form': form}
#     return render(request, 'add_farm_register.html', context)


@login_required(login_url='custom-login')
def delete(request, pk):
    farm = Farm.objects.get(id=pk)
    if request.method == 'POST':
        farm.delete()
        return redirect('farm')
    return render(request, 'delete.html', {'obj': farm})


def pie_chart(request):
    labels = []
    data = []

    queryset = FarmLease.objects.order_by('-farm_id')[:4]
    for farmlease in queryset:
        labels.append(farmlease.farmer_name)
        data.append(farmlease.price)

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })


def total_expenses(request):
    labels = []
    data = []

    queryset = FarmRegister.objects.values('farm_crop_id').annotate(total_cost=Sum('total_cost')).order_by(
        '-quantity')
    for entry in queryset:
        labels.append(entry['farm_crop_id'])
        data.append(entry['total_cost'])

    return render(request, 'farm_register_chart.html', {
        'labels': labels,
        'data': data,
    })


def farm_register_chart(request):
    farm_register_data = FarmRegister.objects.all()
    labels = [d.unit_acre for d in farm_register_data]
    data = [d.total_cost for d in farm_register_data]
    chart_data = {
        'labels': labels,
        'data': data,
    }
    return render(request, 'farm_register_chart.html', {'chart_data': chart_data})

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


# views.py
from django.shortcuts import render
import json


def chart(request):
    expenses = FarmRegister.objects.values_list('category_id', 'total_cost', 'unit_acre')
    earnings = Farm.objects.values_list('name', 'location', 'size')

    chart_data = {
        'labels': [e[0] for e in expenses],
        'datasets': [
            {
                'label': 'Expenses',
                'data': [{'x': e[1], 'y': e[2]} for e in expenses],
                'backgroundColor': 'rgba(255, 99, 132, 0.2)',
                'borderColor': 'rgba(255, 99, 132, 1)',
                'borderWidth': 1
            },
            {
                'label': 'Earnings',
                'data': [{'x': e[1], 'y': e[2]} for e in earnings],
                'backgroundColor': 'rgba(54, 162, 235, 0.2)',
                'borderColor': 'rgba(54, 162, 235, 1)',
                'borderWidth': 1
            }
        ]
    }

    chart_data_json = json.dumps(chart_data)

    return render(request, 'farm_register_chart.html', {'chart_data': chart_data_json})
