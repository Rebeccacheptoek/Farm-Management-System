# Generated by Django 4.1.5 on 2023-01-26 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base_farm", "0007_remove_category_parent_category_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="farmregister",
            name="farm_crop_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="base_farm.farmcrop",
            ),
        ),
    ]