from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('custom-admin/', include('customadmin.urls')),
    path('', include("base_farm.urls")),
    # path('report-builder/', include("report_builder.urls")),
    path('report-builder/', include('report_builder.urls')),
]
