# Generated by Django 4.2.2 on 2024-02-09 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_formdata_salutation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formdata',
            old_name='state',
            new_name='taluka',
        ),
    ]
