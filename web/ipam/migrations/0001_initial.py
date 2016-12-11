# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IPNetwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.GenericIPAddressField()),
                ('size', models.PositiveSmallIntegerField(choices=[(32, '/32 (1 Host)'), (32, '/31 (2 Hosts)'), (30, '/30 (4 Hosts)'), (29, '/29 (8 Hosts)'), (28, '/28 (16 Hosts)'), (27, '/27 (32 Hosts)'), (26, '/26 (64 Hosts)'), (25, '/25 (128 Hosts)'), (24, '/24 (256 Hosts)')])),
                ('description', models.CharField(max_length=500)),
                ('in_use', models.BooleanField()),
            ],
        ),
    ]
