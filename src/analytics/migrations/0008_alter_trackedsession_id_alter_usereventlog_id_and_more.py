# Generated by Django 5.1.4 on 2025-01-06 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0007_auto_20250103_1234"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trackedsession",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="usereventlog",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.DeleteModel(
            name="TrackedPostView",
        ),
    ]
