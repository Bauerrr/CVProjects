# Generated by Django 4.1 on 2023-02-28 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="title",
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]