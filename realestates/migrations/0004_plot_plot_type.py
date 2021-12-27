# Generated by Django 4.0 on 2021-12-09 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestates', '0003_alter_plot_address_alter_plot_plot_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plot',
            name='plot_type',
            field=models.IntegerField(choices=[(0, 'Building'), (1, 'Agricultural'), (2, 'External')], null=True, verbose_name='Plot type'),
        ),
    ]