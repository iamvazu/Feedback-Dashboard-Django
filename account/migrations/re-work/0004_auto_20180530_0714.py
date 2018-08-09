# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-30 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_resources_unutilized_resource'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('company_representative', models.CharField(blank=True, max_length=150)),
                ('company_region', models.CharField(blank=True, max_length=25)),
                ('company_mail', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Months',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=25)),
                ('quarter', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='fourqater',
            name='user',
        ),
        migrations.RemoveField(
            model_name='ongoing',
            name='user',
        ),
        migrations.RemoveField(
            model_name='resources',
            name='user',
        ),
        migrations.DeleteModel(
            name='fourqater',
        ),
        migrations.DeleteModel(
            name='ongoing',
        ),
        migrations.DeleteModel(
            name='resources',
        ),
    ]
