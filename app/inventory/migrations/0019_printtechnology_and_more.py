# Generated by Django 4.1.7 on 2023-04-07 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0018_alter_printermodel_print_color"),
    ]

    operations = [
        migrations.CreateModel(
            name="PrintTechnology",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name="printermodel",
            old_name="print_color",
            new_name="colour_printer",
        ),
        migrations.AlterField(
            model_name="printermodel",
            name="print_technology",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="inventory.printtechnology",
            ),
        ),
    ]
