# Generated by Django 4.1.7 on 2023-02-28 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customadmin", "0011_alter_farmregister_date_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="crop", name="duration", field=models.PositiveIntegerField(),
        ),
    ]
