# Generated by Django 4.0 on 2022-02-15 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realestates', '0002_alter_realestate_plot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realestate',
            name='area',
        ),
    ]
