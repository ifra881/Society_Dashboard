# Generated by Django 4.1.2 on 2023-01-06 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_domain_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='id',
            field=models.AutoField(default=True, primary_key=True, serialize=False),
        ),
    ]
