# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-03 11:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20180603_0724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectcounter',
            name='company',
        ),
        migrations.RemoveField(
            model_name='projectcounter',
            name='month',
        ),
        migrations.RemoveField(
            model_name='projectcounter',
            name='year',
        ),
        migrations.DeleteModel(
            name='ProjectCounter',
        ),
    ]
