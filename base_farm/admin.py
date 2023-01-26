from django.contrib import admin
from .models import Farm, Crop, FarmRegister, Category, FarmCrop, FarmNotes, FarmLease

# Register your models here.
admin.site.register(Farm)
admin.site.register(Crop)
admin.site.register(FarmRegister)
admin.site.register(Category)
admin.site.register(FarmNotes)
admin.site.register(FarmCrop)
admin.site.register(FarmLease)
