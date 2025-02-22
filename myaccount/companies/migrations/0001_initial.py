# Generated by Django 4.2.3 on 2023-07-28 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Companies",
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
                ("company_name", models.CharField(max_length=200)),
                ("boss_name", models.CharField(max_length=200)),
                ("debt", models.IntegerField(default=0)),
                ("credit", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=200)),
                ("debt", models.IntegerField(default=0)),
                ("credit", models.IntegerField(default=0)),
            ],
        ),
    ]
