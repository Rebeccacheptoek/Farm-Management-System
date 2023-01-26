# Generated by Django 4.1.5 on 2023-01-19 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base_farm", "0002_farm_is_mine_farm_size"),
    ]

    operations = [
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
                ("duration", models.DateField()),
            ],
        ),
    ]
