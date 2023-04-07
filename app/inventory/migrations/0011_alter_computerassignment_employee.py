# Generated by Django 4.1.7 on 2023-03-28 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0010_computermodel_manufacturer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="computerassignment",
            name="employee",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="inventory.employee",
            ),
        ),
    ]
