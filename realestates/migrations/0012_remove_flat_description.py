# Generated by Django 4.0 on 2022-02-22 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realestates', '0011_rename_type_realestate_type_realestate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='description',
        ),
    ]