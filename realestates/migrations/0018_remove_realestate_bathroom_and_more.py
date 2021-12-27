# Generated by Django 4.0 on 2021-12-11 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestates', '0017_offer_content_type_offer_object_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realestate',
            name='bathroom',
        ),
        migrations.RemoveField(
            model_name='realestate',
            name='kitchen_type',
        ),
        migrations.RemoveField(
            model_name='realestate',
            name='rooms',
        ),
        migrations.AddField(
            model_name='flat',
            name='bathroom',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Bathroom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flat',
            name='kitchen_type',
            field=models.IntegerField(choices=[(0, 'Kitchen open'), (1, 'Kitchen closed')], default=0, verbose_name='Kitchen'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flat',
            name='rooms',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Rooms'),
            preserve_default=False,
        ),
    ]