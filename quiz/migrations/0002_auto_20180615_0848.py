# Generated by Django 2.0.1 on 2018-06-15 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='no_answer',
            field=models.BooleanField(verbose_name='No'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='yes_answer',
            field=models.BooleanField(verbose_name='Yes'),
        ),
    ]
