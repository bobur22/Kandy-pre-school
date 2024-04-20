# Generated by Django 5.0.3 on 2024-03-27 00:32

import django.utils.timezone
import kandy.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_fname', models.CharField(help_text='Required. The full name of the parrent.', max_length=50)),
                ('parent_address', models.CharField(help_text='Required. The address of the parrent.', max_length=50)),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists'}, help_text='Required. Your gmail address.', max_length=254, validators=[kandy.validators.validate_email], verbose_name='email address')),
                ('home_phone', models.PositiveIntegerField(blank=True, error_messages={'invalid': 'Please enter a valid phone', 'unique': 'A user with that phone number already exists'}, help_text='Enter phone number e.g: +998123456789', unique=True, validators=[kandy.validators.PhoneValidator()], verbose_name='phone number')),
                ('cell_phone', models.PositiveIntegerField(error_messages={'invalid': 'Please enter a valid phone', 'unique': 'A user with that phone number already exists'}, help_text='Enter phone number e.g: +998123456789', validators=[kandy.validators.PhoneValidator()], verbose_name='phone number')),
                ('child_fname', models.CharField(help_text='Required. The full name of the child name.', max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', help_text="Required. Choose child's gender.", max_length=1)),
                ('date_of_birth', models.DateField(blank=True, default=django.utils.timezone.now, help_text="Required. Child's birth date.", null=True)),
                ('child_address', models.CharField(blank=True, help_text='Required. The address of the child', max_length=50, null=True)),
                ('child_img', models.ImageField(blank=True, help_text="'Your child's picture. .jpg, .jpeg, .png only!'", null=True, upload_to='children_photo/')),
                ('child_text', models.TextField(blank=True, help_text='Enter your address here. e.g: 45/9 Sergeli 7, Tashkent Shahar', null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Application',
                'verbose_name_plural': 'Applications',
            },
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(help_text='Required. The full name of the worker.', max_length=50)),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists'}, help_text='Required. Your gmail address.', max_length=254, unique=True, validators=[kandy.validators.validate_email], verbose_name='email address')),
                ('p_number', models.IntegerField(blank=True, error_messages={'invalid': 'Please enter a valid phone', 'unique': 'A user with that phone number already exists'}, help_text='Enter phone number e.g: +998123456789', max_length=13, null=True, unique=True, validators=[kandy.validators.PhoneValidator()], verbose_name='phone number')),
                ('message', models.TextField(blank=True, help_text='Enter your address here. e.g: 45/9 Sergeli 7, Tashkent Shahar', null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Career',
                'verbose_name_plural': 'Careers',
            },
        ),
    ]
