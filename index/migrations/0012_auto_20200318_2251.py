# Generated by Django 2.2.7 on 2020-03-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_character'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='hero_image',
            field=models.ImageField(upload_to='media'),
        ),
    ]