from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('farm/<str:pk>/', views.farm, name="farm"),
    path('create-farm/', views.createFarm, name="create-farm"),
    path('crop/', views.crop, name="crop"),
    path('farm-register/', views.farmRegister, name="farm-register"),
]
