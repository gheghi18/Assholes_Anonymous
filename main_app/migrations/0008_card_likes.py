# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-12 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20171031_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]