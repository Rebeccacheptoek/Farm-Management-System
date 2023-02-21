from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('custom-login/', views.admin_login, name='admin-login'),
    path('update-user/', views.updateUser, name='update-user'),
    path('logout/', views.index, name='logout'),

    path('backend-home/', views.index, name='backend-home'),

    path('b-crop/', views.crop, name='b-crop'),
    path('add-crop/', views.addCrop, name='add-crop'),
    path('edit-crop/<str:pk>', views.updateCrop, name='edit-crop'),

    path('farm/', views.farm, name='farm'),
    path('add-farm/', views.createFarm, name='add-farm'),
    path('edit-farm/<str:pk>', views.updateFarm, name='edit-farm'),

    # path('generate-report/', views.generateReport, name='generate-report'),
    path('report/', views.TotalFarmExpenses, name='report'),

    path('delete/<str:pk>', views.delete, name='delete'),

    # b- for backend
]
