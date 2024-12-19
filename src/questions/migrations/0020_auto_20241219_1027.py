# Generated by Django 3.0.5 on 2024-12-19 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0019_alter_sessionconfig_is_timer_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='start_value',
            field=models.IntegerField(blank=True, help_text='Für Slider: Startwert.', null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='step_value',
            field=models.IntegerField(blank=True, help_text='Für Slider: Stepgröße.', null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='consent',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='question',
            name='max_value',
            field=models.IntegerField(blank=True, help_text='Für Numeric Scale und Slider: Maximaler Wert.', null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='min_value',
            field=models.IntegerField(blank=True, help_text='Für Numeric Scale und Slider: Minimaler Wert.', null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('dropdown', 'Dropdown'), ('multiple_choice', 'Multiple Choice'), ('single_choice', 'Single Choice'), ('numeric', 'Numeric Scale'), ('open_text', 'Open Text'), ('slider', 'Slider'), ('multiple_likert', 'Multiple Likert'), ('fancy_combination', 'Fancy Combination'), ('ampel_rating', 'Ampel Rating')], help_text='Hier bitte den Fragen-Typ festlegen.', max_length=20),
        ),
        migrations.AlterField(
            model_name='sessionconfig',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='text',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]