# Generated by Django 5.0.1 on 2024-01-18 03:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("menuApp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Food",
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
                ("description", models.TextField()),
            ],
        ),
    ]
