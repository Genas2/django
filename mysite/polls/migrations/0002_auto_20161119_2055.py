# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-19 20:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tip',
            old_name='tip',
            new_name='tip_text',
        ),
    ]