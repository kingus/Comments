# Generated by Django 2.2.15 on 2021-07-22 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments_app', '0002_auto_20210722_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='thumbs_down',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='thumbs_up',
            field=models.TextField(default=0),
        ),
    ]
