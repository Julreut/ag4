# Generated by Django 3.0.5 on 2024-12-03 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20241128_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.CharField(default='Default Title', max_length=255, verbose_name='Title'),
        ),
    ]