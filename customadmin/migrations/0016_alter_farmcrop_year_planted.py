# Generated by Django 4.1.7 on 2023-03-09 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customadmin", "0015_alter_farmcrop_planted_on_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="farmcrop", name="year_planted", field=models.IntegerField(),
        ),
    ]
