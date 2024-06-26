# Generated by Django 5.0.3 on 2024-03-27 20:36

import kandy.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kandy', '0003_alter_application_parent_fname_alter_career_f_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='child_address',
            field=models.CharField(blank=True, help_text='The additional address of the child', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='child_fname',
            field=models.CharField(help_text='Required. The full name of the child name.', max_length=50, validators=[kandy.validators.validate_f_name]),
        ),
        migrations.AlterField(
            model_name='career',
            name='p_number',
            field=models.CharField(blank=True, error_messages={'invalid': 'Please enter a valid phone', 'unique': 'A user with that phone number already exists'}, help_text='Enter phone number e.g: +998123456789', max_length=13, null=True, unique=True, validators=[kandy.validators.PhoneValidator], verbose_name='phone number'),
        ),
    ]
