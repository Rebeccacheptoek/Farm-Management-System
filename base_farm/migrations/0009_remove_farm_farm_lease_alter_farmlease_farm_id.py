# Generated by Django 4.1.5 on 2023-01-26 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base_farm", "0008_farmregister_farm_crop_id"),
    ]

    operations = [
        migrations.RemoveField(model_name="farm", name="farm_lease",),
        migrations.AlterField(
            model_name="farmlease",
            name="farm_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="base_farm.farm",
            ),
        ),
    ]