# Generated by Django 4.1.7 on 2023-03-16 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_allresults'),
    ]

    operations = [
        migrations.AddField(
            model_name='allcompetition',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
