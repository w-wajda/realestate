# Generated by Django 4.0 on 2022-02-28 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realestates', '0012_remove_flat_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='garage',
            old_name='type',
            new_name='type_garage',
        ),
        migrations.RemoveField(
            model_name='garage',
            name='description',
        ),
    ]
