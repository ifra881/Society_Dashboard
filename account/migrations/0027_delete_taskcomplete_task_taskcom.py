# Generated by Django 4.1.2 on 2023-01-20 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0026_taskcomplete'),
    ]

    operations = [
        migrations.DeleteModel(
            name='taskcomplete',
        ),
        migrations.AddField(
            model_name='task',
            name='taskcom',
            field=models.BooleanField(default=True, verbose_name='complete'),
        ),
    ]