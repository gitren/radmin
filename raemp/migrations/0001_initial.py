# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 09:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(max_length=10)),
                ('pref', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('address1', models.CharField(max_length=20)),
                ('address2', models.CharField(max_length=20)),
                ('bld', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name_kanji', models.CharField(max_length=20)),
                ('s_name_kanji', models.CharField(max_length=20)),
                ('f_name_kana', models.CharField(max_length=20)),
                ('s_name_kana', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name_kanji', models.CharField(max_length=20)),
                ('shop_name_kana', models.CharField(max_length=20)),
                ('shop_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raemp.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='raemp.Person')),
                ('shop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raemp.Shop')),
            ],
            bases=('raemp.person',),
        ),
        migrations.CreateModel(
            name='TempStaff',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='raemp.Person')),
                ('home_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raemp.Location')),
            ],
            bases=('raemp.person',),
        ),
    ]
