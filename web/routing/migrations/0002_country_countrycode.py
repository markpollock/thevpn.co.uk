# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='countrycode',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
