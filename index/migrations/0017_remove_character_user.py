# Generated by Django 2.2.7 on 2020-03-19 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0016_character'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='user',
        ),
    ]
