# Generated by Django 4.1 on 2023-03-04 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_alter_post_carbs_alter_post_fats_alter_post_kcal_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="carbs",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="fats",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="kcal",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="proteins",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
