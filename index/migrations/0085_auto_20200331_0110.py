# Generated by Django 2.2.7 on 2020-03-30 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0084_auto_20200331_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='users',
            field=models.ManyToManyField(to='index.Author'),
        ),
    ]
