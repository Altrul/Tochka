# Generated by Django 3.2.9 on 2021-11-06 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20211106_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='phone',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='manager',
            name='phone',
            field=models.CharField(default='', max_length=32),
        ),
    ]
