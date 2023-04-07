# Generated by Django 4.1.7 on 2023-04-07 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0016_alter_supplier_email_alter_supplier_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="printermodel",
            name="manufacturer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="inventory.manufacturer",
            ),
        ),
    ]
