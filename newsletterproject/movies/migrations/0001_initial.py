# Generated by Django 4.2.7 on 2023-11-05 12:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                ("name", models.CharField(max_length=100, verbose_name="Film Adı")),
                ("description", models.TextField(verbose_name="Film Açıklaması")),
                ("image", models.CharField(max_length=50, verbose_name="Film Resmi")),
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Eklenme Tarihi"
                    ),
                ),
                ("isPublished", models.BooleanField(default=True)),
            ],
        ),
    ]
