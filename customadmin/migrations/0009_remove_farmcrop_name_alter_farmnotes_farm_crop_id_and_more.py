# Generated by Django 4.1.7 on 2023-02-27 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("customadmin", "0008_alter_farmnotes_farm_crop_id_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="farmcrop", name="name",),
        migrations.AlterField(
            model_name="farmnotes",
            name="farm_crop_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="customadmin.farmcrop",
            ),
        ),
        migrations.AlterField(
            model_name="farmregister",
            name="farm_crop_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="customadmin.farmcrop",
            ),
        ),
    ]
