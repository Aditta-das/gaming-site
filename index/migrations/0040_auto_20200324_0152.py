# Generated by Django 2.2.7 on 2020-03-23 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0039_auto_20200324_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charactercomment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_post', to='index.Character'),
        ),
    ]
