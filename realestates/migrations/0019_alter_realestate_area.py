# Generated by Django 4.0 on 2021-12-11 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestates', '0018_remove_realestate_bathroom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realestate',
            name='area',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Realestete area'),
        ),
    ]