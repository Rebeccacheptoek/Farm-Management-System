# Generated by Django 4.1.7 on 2023-02-27 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customadmin", "0003_farmcrop_primary_key"),
    ]

    operations = [
        migrations.RemoveField(model_name="farmcrop", name="primary_key",),
        migrations.RemoveField(model_name="farmnotes", name="primary_key",),
        migrations.RemoveField(model_name="farmregister", name="primary_key",),
        migrations.AddField(
            model_name="farmcrop",
            name="name",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
