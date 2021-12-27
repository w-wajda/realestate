# Generated by Django 4.0 on 2021-12-11 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestates', '0020_garage_parking_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='balcony_type',
            field=models.IntegerField(choices=[(0, 'Balcony'), (1, 'Loggia'), (2, 'Terrace')], null=True, verbose_name='Balkony type'),
        ),
    ]