# Generated by Django 4.0 on 2021-12-27 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('realestates', '0030_alter_garage_type_alter_offer_object_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('surname', models.CharField(max_length=50, verbose_name='Surname')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('mobile_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Mobile number')),
            ],
        ),
        migrations.AddField(
            model_name='flat',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='garage',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='plot',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='realestate',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='content_type',
            field=models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'realestates'), ('model', 'plot')), models.Q(('app_label', 'realestates'), ('model', 'realestate')), models.Q(('app_label', 'realestates'), ('model', 'flat')), models.Q(('app_label', 'realestates'), ('model', 'garage')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='offer',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='realestates.client', verbose_name='Client'),
        ),
    ]
