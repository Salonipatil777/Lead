# Generated by Django 4.2.2 on 2024-02-09 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_formdata_name_formdata_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdata',
            name='salutation',
            field=models.CharField(max_length=100, null=True),
        ),
    ]