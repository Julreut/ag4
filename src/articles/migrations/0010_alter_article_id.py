# Generated by Django 5.1.4 on 2025-01-06 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0009_auto_20241219_1027"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
