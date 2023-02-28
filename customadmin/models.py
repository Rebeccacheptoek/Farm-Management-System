from django.db import models


# Create your models here.

class Farm(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    size = models.BigIntegerField(null=True)
    location = models.CharField(max_length=200)
    is_mine = models.BooleanField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class FarmLease(models.Model):
    farm_id = models.ForeignKey(Farm, on_delete=models.CASCADE, null=True)
    date_from = models.DateTimeField(auto_now_add=True)
    date_to = models.DateTimeField(auto_now=True)
    farmer_name = models.CharField(max_length=200)
    farmer_phone = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.farm_id, self.farmer_name


class Crop(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    parent_category_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FarmCrop(models.Model):
    farm_id = models.ForeignKey(Farm, on_delete=models.CASCADE, null=True)
    crop_id = models.ForeignKey(Crop, on_delete=models.CASCADE, null=True)
    planted_on = models.DateTimeField(auto_now=True)
    harvested_by = models.CharField(max_length=200)
    year_planted = models.CharField(max_length=50)
    status = models.TextField(blank=True)

    def __str__(self):
        return str(self.farm_id)


class FarmRegister(models.Model):
    farm_crop_id = models.ForeignKey(FarmCrop, on_delete=models.CASCADE, null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    unit_cost = models.CharField(max_length=50)
    unit_acre = models.CharField(max_length=50)
    total_cost = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.farm_crop_id)


class FarmNotes(models.Model):
    farm_crop_id = models.ForeignKey(FarmCrop, on_delete=models.CASCADE, null=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.farm_crop_id)
