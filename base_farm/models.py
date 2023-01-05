from django.db import models

# Create your models here.
class Farm(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    size = models.BigIntegerField
    location = models.CharField(max_length=200)
    is_mine = models.BooleanField
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name