# Generated by Django 4.1.6 on 2023-02-05 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_competition_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='sex',
            field=models.CharField(choices=[('men', 'среди мужчин'), ('women', 'среди женщин')], default='men', max_length=5),
        ),
    ]
