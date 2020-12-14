# Generated by Django 3.1.4 on 2020-12-12 16:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("home", "0002_auto_20201022_2356"),
    ]

    operations = [
        migrations.CreateModel(
            name="Window",
            fields=[
                (
                    "appliance_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="home.appliance",
                    ),
                ),
                ("state", models.BooleanField(verbose_name="state")),
            ],
            options={
                "verbose_name": "Window",
                "verbose_name_plural": "Windows",
            },
            bases=("home.appliance",),
        ),
    ]
