# Generated by Django 4.1.7 on 2023-03-26 10:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0005_remove_computer_category_remove_computer_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="assignment",
            name="quantity",
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
