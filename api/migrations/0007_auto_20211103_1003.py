# Generated by Django 3.2.9 on 2021-11-03 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_meeting_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='token',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='manager',
            name='token',
            field=models.CharField(default='', max_length=36),
        ),
    ]