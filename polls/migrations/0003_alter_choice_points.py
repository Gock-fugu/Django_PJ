# Generated by Django 5.1.5 on 2025-01-21 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='points',
            field=models.FloatField(default=0),
        ),
    ]
