# Generated by Django 2.2.7 on 2020-03-18 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamenews',
            name='slug',
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
    ]
