# Generated by Django 5.1.4 on 2024-12-13 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0014_alter_answer_unique_together_answer_sub_question_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="name",
            field=models.TextField(
                blank=True, help_text="Hier bitte den Item-Name festlegen."
            ),
        ),
    ]
