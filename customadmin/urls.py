from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('custom-login/', views.admin_login, name='admin-login'),
    path('home/', views.index, name='home'),
]
