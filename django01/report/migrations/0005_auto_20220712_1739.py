# Generated by Django 3.2.5 on 2022-07-12 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_auto_20220712_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicuser',
            name='security_answer',
            field=models.CharField(help_text='Enter the answer to the above security question.', max_length=50, verbose_name='Security Answer'),
        ),
        migrations.AlterField(
            model_name='publicuser',
            name='security_question',
            field=models.CharField(help_text='Enter a security question that only you will know the answer to.', max_length=255, verbose_name='Security Question'),
        ),
    ]