# Generated by Django 4.0 on 2022-02-22 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realestates', '0010_remove_plot_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realestate',
            old_name='type',
            new_name='type_realestate',
        ),
        migrations.RemoveField(
            model_name='realestate',
            name='description',
        ),
    ]
