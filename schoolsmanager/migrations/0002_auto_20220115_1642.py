# Generated by Django 3.2 on 2022-01-15 16:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolsmanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='maxstudents',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Maximum Number of Students Allowed'),
        ),
        migrations.AlterField(
            model_name='school',
            name='schoolname',
            field=models.CharField(max_length=20, verbose_name='School Name'),
        ),
    ]
