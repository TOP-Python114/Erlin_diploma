# Generated by Django 4.1.6 on 2023-02-12 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_armwrestler_grade_armwrestler_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='armwrestler',
            name='team',
            field=models.CharField(default='Новосибирск', max_length=4),
        ),
    ]