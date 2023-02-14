from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .forms import CropForm


# Create your views here.
def admin_login(request):
    # response = HttpResponseRedirect("Hello backend world")
    # return render(request, 'login.html')
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


def index(request):
    return render(request, 'index.html')


def crop(request):
    return render(request, 'crop.html')


def generateReport(request):
    return render(request, 'generate_report.html')


def farm(request):
    return render(request, 'farm.html')


def addCrop(request):
    form = CropForm()
    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('b-crop')
    context = {'form': form}
    return render(request, 'add_crop.html', context)

