# Generated by Django 2.2.7 on 2020-03-31 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0088_auto_20200331_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='current_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
