# Generated by Django 3.0.5 on 2025-02-04 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0015_auto_20250123_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='is_active',
            field=models.BooleanField(default=False, help_text='Markiert die aktive Konfiguration'),
        ),
    ]
