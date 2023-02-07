from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', include('customadmin.urls')),
    path('custom-admin/', admin.site.urls),
    path('', include("base_farm.urls"))
]
