# Generated by Django 4.0.3 on 2022-03-16 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivlichen', '0007_rename_outside_inventory_observation_outside_scope'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='observation',
            name='fine_substrate',
        ),
        migrations.AddField(
            model_name='observation',
            name='host',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
