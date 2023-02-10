from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('custom-login/', views.admin_login, name='admin-login'),
    path('backend-home/', views.index, name='back-home'),
    path('logout/', views.index, name='logout'),
]
