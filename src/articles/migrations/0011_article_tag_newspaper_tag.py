# Generated by Django 5.1.4 on 2025-01-09 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0010_alter_article_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="tag",
            field=models.CharField(default="control", max_length=50),
        ),
        migrations.AddField(
            model_name="newspaper",
            name="tag",
            field=models.CharField(default="control", max_length=50),
        ),
    ]
