# Generated by Django 4.0 on 2021-12-27 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realestates', '0022_alter_flat_balcony_type_alter_flat_bathroom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plot',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestates.address', verbose_name='Plot address'),
        ),
    ]
