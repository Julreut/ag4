# Generated by Django 3.0.5 on 2025-03-09 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0016_configuration_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuration',
            name='registration_enabled',
        ),
    ]
