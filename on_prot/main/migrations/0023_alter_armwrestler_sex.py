# Generated by Django 4.1.6 on 2023-04-11 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_allresults_weight_actual_alter_armwrestler_grade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armwrestler',
            name='sex',
            field=models.CharField(choices=[('m', 'мужчина'), ('w', 'женщина')], max_length=2),
        ),
    ]
