# Generated by Django 5.0.3 on 2024-03-27 00:37

import kandy.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kandy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='cell_phone',
            field=models.CharField(error_messages={'invalid': 'Please enter a valid phone', 'unique': 'A user with that phone number already exists'}, help_text='Enter phone number e.g: +998123456789', max_length=13, validators=[kandy.validators.PhoneValidator()], verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='application',
            name='home_phone',
            field=models.CharField(blank=True, error_messages={'invalid': 'Please enter a valid phone', 'unique': 'A user with that phone number already exists'}, help_text='Enter phone number e.g: +998123456789', max_length=13, unique=True, validators=[kandy.validators.PhoneValidator()], verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='career',
            name='p_number',
            field=models.CharField(blank=True, error_messages={'invalid': 'Please enter a valid phone', 'unique': 'A user with that phone number already exists'}, help_text='Enter phone number e.g: +998123456789', max_length=13, null=True, unique=True, validators=[kandy.validators.PhoneValidator()], verbose_name='phone number'),
        ),
    ]
