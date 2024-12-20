# Generated by Django 5.1.4 on 2024-12-12 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0009_text_visibility"),
    ]

    operations = [
        migrations.AlterField(
            model_name="text",
            name="content",
            field=models.TextField(help_text="Plain text content."),
        ),
        migrations.AlterField(
            model_name="text",
            name="identifier",
            field=models.CharField(
                choices=[
                    ("end_experiment_header_de", "End Experiment Header (German)"),
                    ("end_experiment_header_en", "End Experiment Header (English)"),
                    ("end_experiment_message_de", "End Experiment Message (German)"),
                    ("end_experiment_message_en", "End Experiment Message (English)"),
                    (
                        "participant_info_header_de",
                        "Participant Information Header (German)",
                    ),
                    (
                        "participant_info_header_en",
                        "Participant Information Header (English)",
                    ),
                    (
                        "participant_info_message_de",
                        "Participant Information Message (German)",
                    ),
                    (
                        "participant_info_message_en",
                        "Participant Information Message (English)",
                    ),
                    ("consent_form_header_de", "Consent Form Header (German)"),
                    ("consent_form_header_en", "Consent Form Header (English)"),
                    ("consent_form_message_de", "Consent Form Message (German)"),
                    ("consent_form_message_en", "Consent Form Message (English)"),
                ],
                help_text="Choose which text to display.",
                max_length=200,
                unique=True,
            ),
        ),
    ]
