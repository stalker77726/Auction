# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-11 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_auto_20170611_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot_sub',
            name='is_open',
            field=models.BooleanField(default=True),
        ),
    ]