# Generated by Django 3.2.9 on 2021-11-05 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_manager_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='manager',
        ),
        migrations.AddField(
            model_name='meeting',
            name='manager_token',
            field=models.CharField(default='', max_length=36),
        ),
    ]
