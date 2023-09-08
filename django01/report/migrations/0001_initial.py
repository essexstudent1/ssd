# Generated by Django 3.2.14 on 2022-07-11 17:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('firstName', models.CharField(help_text='Enter your first name.', max_length=100, verbose_name='First Name')),
                ('lastName', models.CharField(help_text='Enter your last name.', max_length=100, verbose_name='Last Name')),
                ('email', models.EmailField(help_text='Enter your email address.', max_length=100, unique=True, verbose_name='Email Address')),
                ('username', models.CharField(help_text='Enter a username.', max_length=100, unique=True, verbose_name='Username')),
                ('address', models.CharField(help_text='Enter your street name and number, including unit number if applicable.', max_length=100, verbose_name='Street Address')),
                ('town', models.CharField(help_text='Enter your city, town, or village.', max_length=100, verbose_name='City or town')),
                ('province', models.CharField(help_text='Enter your state or province.', max_length=100, verbose_name='State or Province')),
                ('country', models.CharField(help_text='Enter your country.', max_length=100, verbose_name='Country')),
                ('postcode', models.CharField(help_text='Enter your postal code.', max_length=100, verbose_name='Postal Code')),
                ('is_superuser', models.BooleanField(default=False)),
                ('registeredOn', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]