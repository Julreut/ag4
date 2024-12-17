# Generated by Django 5.1.4 on 2024-12-17 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0015_question_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="choices",
            field=models.TextField(
                blank=True,
                help_text="Für alle Fragen mit vordefinierten Antworten: Komma-separierte Auswahlmöglichkeiten.",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="max_value",
            field=models.IntegerField(
                blank=True, help_text="Für Numeric Scale: Maximaler Wert.", null=True
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="min_value",
            field=models.IntegerField(
                blank=True, help_text="Für Numeric Scale: Minimaler Wert.", null=True
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="name",
            field=models.TextField(
                blank=True,
                help_text="Hier bitte den Item-Name festlegen (fuer die Datenauswertung).",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="question_text",
            field=models.TextField(
                help_text="Welche Frage soll in diesem Item gestellt werden?"
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="question_type",
            field=models.CharField(
                choices=[
                    ("dropdown", "Dropdown"),
                    ("likert", "Likert Scale"),
                    ("multiple_choice", "Multiple Choice"),
                    ("single_choice", "Single Choice"),
                    ("numeric", "Numeric Scale"),
                    ("open_text", "Open Text"),
                    ("slider", "Slider"),
                    ("multiple_likert", "Multiple Likert"),
                    ("fancy_combination", "Fancy Combination"),
                    ("ampel_rating", "Ampel Rating"),
                ],
                help_text="Hier bitte den Fragen-Typ festlegen.",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="required",
            field=models.BooleanField(default=True, help_text="Pflichtfrage?"),
        ),
        migrations.AlterField(
            model_name="question",
            name="sub_questions",
            field=models.TextField(
                blank=True,
                help_text="Für Multiple Likert und Fancy Combination: Komma-separierte Sub-Fragen.",
            ),
        ),
    ]
