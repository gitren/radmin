# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-05 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import raemp.models


class Migration(migrations.Migration):

    dependencies = [
        ('raemp', '0005_auto_20171101_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='file',
        ),
        migrations.AddField(
            model_name='image',
            name='image_file',
            field=models.ImageField(default=None, upload_to=raemp.models.Image.get_image_path, verbose_name='画像ファイル'),
        ),
        migrations.AddField(
            model_name='image',
            name='image_type',
            field=models.CharField(choices=[('0', '写メ'), ('1', '証明書')], default=None, max_length=1),
        ),
    ]
