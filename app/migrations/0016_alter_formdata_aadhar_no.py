# Generated by Django 4.2.2 on 2024-02-09 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_formdata_type_of_members_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdata',
            name='aadhar_no',
            field=models.CharField(max_length=30),
        ),
    ]
