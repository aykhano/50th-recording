# Generated by Django 5.1.6 on 2025-03-03 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_task_created_at_task_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='label',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
