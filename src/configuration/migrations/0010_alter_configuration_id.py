# Generated by Django 5.1.4 on 2024-12-11 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("configuration", "0009_configuration_relationship_management_enabled"),
    ]

    operations = [
        migrations.AlterField(
            model_name="configuration",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]