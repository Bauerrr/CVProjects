# Generated by Django 4.1.7 on 2023-03-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Submission",
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
                ("date", models.DateTimeField(auto_now_add=True)),
                ("who", models.CharField(max_length=200)),
                ("what", models.CharField(max_length=2000)),
                ("where", models.CharField(max_length=200)),
            ],
        ),
    ]
