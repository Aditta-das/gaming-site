# Generated by Django 2.2.7 on 2020-03-24 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0051_auto_20200325_0008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=150)),
                ('paragraph', models.CharField(max_length=200)),
            ],
        ),
    ]
