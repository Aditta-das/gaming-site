# Generated by Django 2.2.7 on 2020-03-28 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0073_gamenews_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
