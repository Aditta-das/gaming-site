# Generated by Django 2.2.7 on 2020-03-30 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0085_auto_20200331_0110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='current_user',
        ),
    ]
