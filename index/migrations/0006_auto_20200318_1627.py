# Generated by Django 2.2.7 on 2020-03-18 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20200318_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamesinglenews',
            name='user',
        ),
        migrations.DeleteModel(
            name='GameNews',
        ),
        migrations.DeleteModel(
            name='GameSingleNews',
        ),
    ]
