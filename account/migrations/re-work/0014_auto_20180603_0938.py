# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-03 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_projectcounter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcounter',
            name='adiva_incurred_hours',
            field=models.IntegerField(verbose_name='Adiva Incurred Hours'),
        ),
    ]