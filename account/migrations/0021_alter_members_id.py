# Generated by Django 4.1.2 on 2023-01-18 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_alter_members_domain_delete_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
