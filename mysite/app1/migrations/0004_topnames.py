# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2015-12-29 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20151229_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='topnames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=200)),
            ],
        ),
    ]
