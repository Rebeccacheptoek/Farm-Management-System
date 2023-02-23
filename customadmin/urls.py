from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('custom-login/', views.admin_login, name='admin-login'),
    path('update-user/', views.updateUser, name='update-user'),
    path('', views.index, name='home'),
    path('logout/', views.index, name='logout'),

    path('backend-home/', views.index, name='backend-home'),

    path('b-crop/', views.crop, name='b-crop'),
    path('view-crop/<str:pk>', views.viewCrop, name='view-crop'),
    path('add-crop/', views.addCrop, name='add-crop'),
    path('edit-crop/<str:pk>', views.updateCrop, name='edit-crop'),

    path('farm/', views.farm, name='farm'),
    path('add-farm/', views.createFarm, name='add-farm'),
    path('edit-farm/<str:pk>', views.updateFarm, name='edit-farm'),

    path('category', views.category, name='category'),
    path('add-category', views.addCategory, name='add-category'),

    path('farm-notes', views.farmNote, name='farm-note'),
    path('add-farm-notes', views.addFarmNote, name='add-farm-note'),

    path('farm-lease', views.farmLease, name='farm-lease'),
    path('add-farm-lease', views.addFarmLease, name='add-farm-lease'),

    path('farm-crop', views.farmCrop, name='farm-crop'),
    path('add-farm-crop', views.addFarmCrop, name='add-farm-crop'),


    path('farm-register/', views.farmRegister, name='farm-register'),
    path('add-farm-register/', views.addFarmRegister, name='add-farm-register'),

    # path('generate-report/', views.generateReport, name='generate-report'),
    # path('report/', views.TotalFarmExpenses, name='report'),

    path('delete/<str:pk>', views.delete, name='delete'),

    # b- for backend
]
