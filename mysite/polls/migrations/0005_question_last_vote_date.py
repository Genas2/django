# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 23:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20161123_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='last_vote_date',
            field=models.DateTimeField(auto_now=True, verbose_name='last vote date'),
        ),
    ]
