# Generated by Django 5.1.4 on 2024-12-17 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0017_question_sub_choices_alter_question_choices_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="sessionconfig",
            name="is_timer_enabled",
            field=models.BooleanField(
                default=True, help_text="Timer aktivieren oder deaktivieren"
            ),
        ),
    ]
