# Generated by Django 4.1.5 on 2023-02-14 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Crop",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True, null=True)),
                ("duration", models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name="Farm",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True, null=True)),
                ("size", models.BigIntegerField(null=True)),
                ("location", models.CharField(max_length=200)),
                ("is_mine", models.BooleanField(blank=True, null=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="FarmCrop",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("planted_on", models.DateTimeField(auto_now=True)),
                ("harvested_by", models.CharField(max_length=200)),
                ("year_planted", models.CharField(max_length=50)),
                ("status", models.TextField(blank=True)),
                (
                    "crop_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customadmin.crop",
                    ),
                ),
                (
                    "farm_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customadmin.farm",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FarmRegister",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("unit_cost", models.CharField(max_length=50)),
                ("unit_acre", models.CharField(max_length=50)),
                ("total_cost", models.CharField(max_length=50)),
                ("quantity", models.CharField(max_length=50)),
                ("description", models.TextField(blank=True, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                (
                    "category_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customadmin.category",
                    ),
                ),
                (
                    "farm_crop_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customadmin.farmcrop",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FarmNotes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("notes", models.TextField(blank=True, null=True)),
                (
                    "farm_crop_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customadmin.farmcrop",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FarmLease",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_from", models.DateTimeField(auto_now_add=True)),
                ("date_to", models.DateTimeField(auto_now=True)),
                ("farmer_name", models.CharField(max_length=200)),
                ("farmer_phone", models.CharField(max_length=50)),
                ("price", models.IntegerField()),
                (
                    "farm_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customadmin.farm",
                    ),
                ),
            ],
        ),
    ]
