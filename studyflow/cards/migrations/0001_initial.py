# Generated by Django 5.0.2 on 2024-02-13 01:58

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Card",
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
                ("front_side", models.TextField()),
                ("back_side", models.TextField()),
                (
                    "next_time",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "knowledge_level",
                    models.PositiveSmallIntegerField(default=0),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cards",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
