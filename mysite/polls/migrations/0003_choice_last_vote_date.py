# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-23 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20161119_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='last_vote_date',
            field=models.DateTimeField(auto_now=True, verbose_name='last vote date'),
        ),
    ]
