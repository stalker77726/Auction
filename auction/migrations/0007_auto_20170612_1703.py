# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0006_lotrate'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot_sub',
            name='winner',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lot_sub',
            name='starting_price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='lotrate',
            name='rate',
            field=models.PositiveIntegerField(),
        ),
    ]