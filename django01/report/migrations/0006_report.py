# Generated by Django 4.0.6 on 2022-07-15 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_auto_20220712_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.IntegerField(max_length=11)),
                ('data_breach_details', models.CharField(max_length=1000)),
                ('responsible_party', models.CharField(max_length=1000)),
                ('others_notified', models.IntegerField(max_length=1)),
                ('data_breach_noticed_on', models.DateField()),
            ],
        ),
    ]
