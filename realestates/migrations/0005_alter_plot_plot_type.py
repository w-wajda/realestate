# Generated by Django 4.0 on 2021-12-09 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestates', '0004_plot_plot_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plot',
            name='plot_type',
            field=models.IntegerField(choices=[(0, 'Building'), (1, 'Agricultural'), (2, 'External')], verbose_name='Plot type'),
        ),
    ]