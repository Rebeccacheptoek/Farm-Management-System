from django.contrib import admin
from django.urls import path


# Register your models here.


# Define custom URLs for the admin interface
urlpatterns = [
    path('admin/', admin.site.urls),
]
