# Generated by Django 3.0.5 on 2024-12-11 16:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0002_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='demographic_type',
        ),
        migrations.AlterField(
            model_name='question',
            name='choices',
            field=models.TextField(blank=True, help_text='Komma-separierte Auswahlmöglichkeiten für Fragen mit vordefinierten Antworten (z.B. Dropdown, Likert-Skala).'),
        ),
        migrations.AlterField(
            model_name='question',
            name='label',
            field=models.CharField(choices=[('before', 'Before'), ('after', 'After')], help_text='Gibt an, ob die Frage vor oder nach dem Experiment gestellt wird.', max_length=10),
        ),
        migrations.AlterField(
            model_name='question',
            name='max_value',
            field=models.IntegerField(blank=True, help_text='Maximaler Wert für numerische Fragen.', null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='min_value',
            field=models.IntegerField(blank=True, help_text='Minimaler Wert für numerische Fragen.', null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(help_text='Der Text der Frage.'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('dropdown', 'Dropdown'), ('likert', 'Likert Scale'), ('multiple_choice', 'Multiple Choice'), ('single_choice', 'Single Choice'), ('numeric', 'Numeric Scale'), ('open_text', 'Open Text')], help_text='Der Typ der Frage.', max_length=20),
        ),
        migrations.AlterField(
            model_name='question',
            name='required',
            field=models.BooleanField(default=True, help_text='Ob die Frage beantwortet werden muss.'),
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together={('question', 'user')},
        ),
    ]
