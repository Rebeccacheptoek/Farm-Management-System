import random
from django.contrib import messages
from django.db.models import Sum
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Crop, Farm, FarmRegister, FarmCrop, FarmLease, FarmNotes, Category
from .forms import *
from django.views.generic import TemplateView
import pdb
from django.views import View
from chartjs.views.lines import BaseLineChartView



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


@login_required(login_url='custom-login')
def delete(request, pk):
    farm = Farm.objects.get(id=pk)
    if request.method == 'POST':
        farm.delete()
        return redirect('farm')
    return render(request, 'delete.html', {'obj': farm})


@login_required(login_url='custom-login')
def delete(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category')
    return render(request, 'delete.html', {'obj': category})


def farm_lease_pie_chart(request):
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


def farm_expense_pie_chart(request):
    labels = []
    data = []

    queryset = FarmRegister.objects.order_by('-farm_crop_id')[:4]
    for farmregister in queryset:
        labels.append(farmregister.category_id)
        data.append(farmregister.total_cost)

    return render(request, 'farm_register_expense.html', {
        'labels': labels,
        'data': data,
    })


def farm_report(request):
    categories = Category.objects.all()
    category_totals = {}
    for category in categories:
        total_cost = FarmRegister.objects.filter(category_id=category.id).aggregate(Sum('total_cost'))['total_cost__sum'] or 0
        category_totals[category.name] = total_cost

    # prepare the data for the chart
    labels = list(category_totals.keys())
    values = list(category_totals.values())

    return render(request, 'farm_register_expense.html',  {'labels': labels, 'values': values})


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


def report_view(request):
    # Get all the parent categories
    parent_categories = Category.objects.filter(parent_category=None)

    # Create an empty dictionary to store the report data
    report_data = {}

    # Loop through each parent category and calculate the total expenses and earnings
    for parent_category in parent_categories:
        # Get all the child categories for the parent category
        child_categories = Category.objects.filter(parent_category=parent_category)

        # Create an empty dictionary to store the category report data
        category_report_data = {}

        # Loop through each child category and calculate the total expenses and earnings
        for child_category in child_categories:
            # Get all the farm register entries for the child category
            category_entries = FarmRegister.objects.filter(category_id__parent_category__name='Expenses',
                                                           category_id=child_category)

            # Calculate the total expenses and earnings for the child category
            total_expenses = 0
            total_earnings = 0

            for entry in category_entries:
                total_expenses += entry.total_cost if entry.expense.category == child_category else 0
                total_earnings += entry.total_cost if entry.earning.category == child_category else 0

            # Add the data to the category report dictionary
            category_report_data[child_category.name] = {'total_expenses': total_expenses,
                                                         'total_earnings': total_earnings}

        # Add the category report data to the main report dictionary
        report_data[parent_category.name] = category_report_data

    # Pass the report data to the template for display
    return render(request, 'add_crop.html', {'report_data': report_data})


def chart_view(request):
    # Get the report data
    report_data = {}

    parent_categories = Category.objects.filter(parent=None)

    for parent_category in parent_categories:
        child_categories = Category.objects.filter(parent=parent_category)

        for child_category in child_categories:
            category_entries = FarmRegister.objects.filter(expense__category=child_category,
                                                           earning__category=child_category)

            total_expenses = 0
            total_earnings = 0

            for entry in category_entries:
                total_expenses += entry.total_cost if entry.expense.category == child_category else 0
                total_earnings += entry.total_cost if entry.earning.category == child_category else 0

            if parent_category.name not in report_data:
                report_data[parent_category.name] = {}

            report_data[parent_category.name][child_category.name] = {'total_expenses': total_expenses,
                                                                      'total_earnings': total_earnings}

    # Convert the report data to a format that can be used in a chart
    chart_data = {'labels': [], 'datasets': []}

    for parent_category_name, category_report_data in report_data.items():
        for child_category_name, data in category_report_data.items():
            if child_category_name not in chart_data['labels']:
                chart_data['labels'].append(child_category_name)

            if parent_category_name not in [dataset['label'] for dataset in chart_data['datasets']]:
                # Generate a random color for the dataset
                color = random.randint(0, 16777215)
                chart_data['datasets'].append(
                    {'label': parent_category_name, 'data': [], 'backgroundColor': f"#{color:06x}"})

            dataset_index = [dataset['label'] for dataset in chart_data['datasets']].index(parent_category_name)
            chart_data['datasets'][dataset_index]['data'].append(data['total_earnings'] - data['total_expenses'])

    # Convert the chart data to a JSON response
    return JsonResponse(chart_data)


def category_list(request):
    parent_categories = Category.objects.filter(parent=None).annotate(
        total_expenses=Sum('farmregister__ploughing_fee', 'farmregister__fertilizer_cost',
                           'farmregister__planting_cost'),
        total_earnings=Sum('farm__maize_sale', 'farm__bean_sale'),
    )
    context = {'parent_categories': parent_categories}
    return render(request, 'add_crop.html', context)
