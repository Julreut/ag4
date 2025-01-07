# Generated by Django 5.1.4 on 2025-01-07 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "questions",
            "0021_alter_answer_id_alter_consent_id_alter_question_id_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="choices",
            field=models.TextField(
                blank=True,
                help_text="Für alle Fragen mit vordefinierten Antworten. Für Slider bitte genau drei Möglichkeiten passend zu den min und max values angeben: Semikolon-separierte Auswahlmöglichkeiten.",
            ),
        ),
    ]
