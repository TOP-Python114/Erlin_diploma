# Generated by Django 4.1.6 on 2023-02-26 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_armwrestler_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armwrestler',
            name='team',
            field=models.CharField(default='Новосибирск', max_length=54),
        ),
    ]
