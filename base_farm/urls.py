from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginPage, name='login'),
    path('end-user/', views.endUser, name='end-user'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.home, name="home"),
    path('front-farm/<str:pk>/', views.farm, name="farm"),
    path('create-farm/', views.createFarm, name="create-farm"),
    path('update-farm/<str:pk>/', views.updateFarm, name="update-farm"),
    path('delete-farm/<str:pk>/', views.deleteFarm, name="delete-farm"),
    path('crop/', views.crop, name="crop"),
    path('farm-registration/', views.farmRegister, name="farm-registration"),
]
