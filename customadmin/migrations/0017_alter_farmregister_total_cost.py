# Generated by Django 4.1.7 on 2023-03-11 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customadmin", "0016_alter_farmcrop_year_planted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="farmregister",
            name="total_cost",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]