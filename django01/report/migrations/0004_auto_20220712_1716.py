# Generated by Django 3.2.5 on 2022-07-12 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_rename_user_publicuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicuser',
            old_name='registeredOn',
            new_name='date_joined',
        ),
        migrations.AddField(
            model_name='publicuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='publicuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
