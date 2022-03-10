# Generated by Django 4.0.3 on 2022-03-06 22:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ivlichen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 3, 6, 22, 21, 30, 6592, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='observation',
            name='locality',
            field=models.CharField(default=None, max_length=125, null=True),
        ),
    ]
