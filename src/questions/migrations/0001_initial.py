# Generated by Django 3.0.5 on 2024-12-11 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(choices=[('before', 'Before'), ('after', 'After')], max_length=10)),
                ('question_text', models.TextField()),
                ('question_type', models.CharField(choices=[('demographic', 'Demographic Question'), ('likert', 'Likert Scale'), ('multiple_choice', 'Multiple Choice'), ('single_choice', 'Single Choice'), ('numeric', 'Numeric Scale'), ('open_text', 'Open Text')], max_length=20)),
                ('demographic_type', models.CharField(blank=True, choices=[('age', 'Age'), ('gender', 'Gender'), ('education', 'Education'), ('income', 'Income'), ('occupation', 'Occupation'), ('nationality', 'Nationality')], help_text='Specify if this is a demographic question.', max_length=20, null=True)),
                ('choices', models.TextField(blank=True, help_text='Comma-separated choices for multiple-choice or Likert scale questions.')),
                ('min_value', models.IntegerField(blank=True, help_text='Minimum value for numeric questions.', null=True)),
                ('max_value', models.IntegerField(blank=True, help_text='Maximum value for numeric questions.', null=True)),
                ('required', models.BooleanField(default=True)),
            ],
        ),
    ]
