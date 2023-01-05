from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('farm/<str:pk>/', views.farm, name="farm"),
]
