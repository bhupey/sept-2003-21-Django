# Generated by Django 4.2.5 on 2023-09-26 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("temp_inheritance", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="StudentProfile",
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
                ("contact", models.CharField(max_length=20)),
                ("address", models.CharField(max_length=20)),
                ("roll_no", models.IntegerField()),
                (
                    "student",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="temp_inheritance.student",
                    ),
                ),
            ],
        ),
    ]
