# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-30 15:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raemp', '0003_auto_20170912_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='person_address',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='raemp.Location', verbose_name='住所'),
        ),
        migrations.AlterField(
            model_name='location',
            name='address1',
            field=models.CharField(max_length=20, verbose_name='住所１'),
        ),
        migrations.AlterField(
            model_name='location',
            name='address2',
            field=models.CharField(max_length=20, verbose_name='住所２'),
        ),
        migrations.AlterField(
            model_name='location',
            name='bld',
            field=models.CharField(blank=True, max_length=20, verbose_name='建物等'),
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=20, verbose_name='市区群町村'),
        ),
        migrations.AlterField(
            model_name='location',
            name='pref',
            field=models.CharField(max_length=20, verbose_name='都道府県'),
        ),
        migrations.AlterField(
            model_name='location',
            name='zip_code',
            field=models.CharField(max_length=10, verbose_name='郵便番号'),
        ),
        migrations.AlterField(
            model_name='person',
            name='f_name_kana',
            field=models.CharField(max_length=20, verbose_name='名前（カナ）'),
        ),
        migrations.AlterField(
            model_name='person',
            name='f_name_kanji',
            field=models.CharField(max_length=20, verbose_name='名前（漢字）'),
        ),
        migrations.AlterField(
            model_name='person',
            name='s_name_kana',
            field=models.CharField(max_length=20, verbose_name='姓（カナ）'),
        ),
        migrations.AlterField(
            model_name='person',
            name='s_name_kanji',
            field=models.CharField(max_length=20, verbose_name='姓（漢字）'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raemp.Location', verbose_name='住所'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_name_kana',
            field=models.CharField(max_length=20, verbose_name='店舗名称（カナ）'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_name_kanji',
            field=models.CharField(max_length=20, verbose_name='店舗名称（漢字）'),
        ),
    ]