# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0015_lot_sub_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot_sub',
            name='image',
            field=models.ImageField(null=True, upload_to='ads/'),
        ),
    ]
