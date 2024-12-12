# Generated by Django 5.1.4 on 2024-12-11 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0005_experimentdocument"),
    ]

    operations = [
        migrations.CreateModel(
            name="Text",
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
                (
                    "identifier",
                    models.CharField(
                        help_text="A unique identifier for this text (e.g., 'end_experiment_header').",
                        max_length=100,
                        unique=True,
                    ),
                ),
                (
                    "content",
                    models.TextField(help_text="The HTML or plain text content."),
                ),
            ],
        ),
    ]