# Generated by Django 4.1.6 on 2023-04-12 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_armwrestler'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]
