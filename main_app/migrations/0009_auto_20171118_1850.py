# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-18 17:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import random
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_card_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='title',
            field=models.CharField(default='No Title', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='collection',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]