# Generated by Django 4.1.7 on 2023-03-17 03:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_allcompetition_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allresults',
            name='hand',
        ),
        migrations.AddField(
            model_name='allresults',
            name='left',
            field=models.PositiveIntegerField(default=100, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='allresults',
            name='right',
            field=models.PositiveIntegerField(default=100, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='allresults',
            name='place',
            field=models.PositiveIntegerField(default=100, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
