# Generated by Django 5.0.2 on 2024-02-24 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_remove_photosubmission_capture_datetime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photosubmission',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='photosubmission',
            name='longitude',
        ),
    ]
