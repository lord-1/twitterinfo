# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2015-12-29 10:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_tweet'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tweet',
            new_name='tweets',
        ),
    ]
