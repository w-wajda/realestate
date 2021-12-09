# Generated by Django 4.0 on 2021-12-09 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realestates', '0010_realestate_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=60, null=True)),
                ('area', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('price', models.PositiveSmallIntegerField(default=0, null=True)),
                ('rooms', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('kitchen', models.CharField(blank=True, choices=[('OPEN', 'open'), ('CLOSED', 'closed')], max_length=6, null=True)),
                ('bathroom', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('number_floors', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('floor_number', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('year_built', models.DateField(blank=True, null=True)),
                ('garage', models.CharField(blank=True, choices=[('YES', 'yes'), ('NO', 'no')], max_length=3, null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='realestates.address')),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=60, null=True)),
                ('area', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('area_land', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('price', models.PositiveSmallIntegerField(default=0, null=True)),
                ('rooms', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('kitchen', models.CharField(blank=True, choices=[('OPEN', 'open'), ('CLOSED', 'closed')], max_length=6, null=True)),
                ('bathroom', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('number_floors', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('year_built', models.DateField(blank=True, null=True)),
                ('garage', models.CharField(blank=True, choices=[('YES', 'yes'), ('NO', 'no')], max_length=3, null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='realestates.address')),
            ],
        ),
        migrations.DeleteModel(
            name='Realestate',
        ),
    ]
