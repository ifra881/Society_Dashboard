# Generated by Django 4.1.2 on 2023-01-20 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0031_alter_task_completion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='completion',
            new_name='completion_date',
        ),
    ]
