# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-06 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raemp', '0006_auto_20171105_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_type',
            field=models.CharField(choices=[('0', '写メ'), ('1', '証明書')], default=None, max_length=1, verbose_name='画像種類'),
        ),
    ]
