# Generated by Django 5.1.4 on 2025-01-09 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0010_profile_condition_tag"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="condition_tag",
        ),
    ]
