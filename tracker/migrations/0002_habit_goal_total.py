# Generated by Django 5.2.3 on 2025-06-28 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='goal_total',
            field=models.PositiveIntegerField(blank=True, help_text='Optional total completions goal', null=True),
        ),
    ]
