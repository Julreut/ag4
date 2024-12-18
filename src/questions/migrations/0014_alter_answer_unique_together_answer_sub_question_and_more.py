# Generated by Django 5.1.4 on 2024-12-13 11:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0013_question_sub_questions_alter_question_question_type"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="answer",
            unique_together=set(),
        ),
        migrations.AddField(
            model_name="answer",
            name="sub_question",
            field=models.CharField(
                blank=True,
                help_text="Optional: Sub-question identifier for formats like Multiple Likert or Fancy Combination.",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="answer",
            unique_together={("question", "user", "sub_question")},
        ),
    ]