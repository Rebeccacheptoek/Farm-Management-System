from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('custom-login/', views.admin_login, name='admin-login'),
    # path('backend-home/', views.index, name='back-home'),
    path('logout/', views.index, name='logout'),
    path('b-crop/', views.crop, name='b-crop'),
    path('generate-report/', views.generateReport, name='generate-report'),
    path('farm/', views.farm, name='farm'),
    path('add-farm/', views.createFarm, name='add-farm'),
    path('add-crop/', views.addCrop, name='add-crop'),


    # b- for backend
]
