# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-06 02:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, verbose_name='Company Name')),
                ('company_representative', models.CharField(blank=True, max_length=150, verbose_name='Company Representative')),
                ('company_region', models.CharField(blank=True, max_length=25, verbose_name='Company Location')),
                ('company_mail', models.CharField(blank=True, max_length=100, verbose_name='Company Name')),
                ('company_representative_designation', models.CharField(blank=True, max_length=100, verbose_name='Representative Designation')),
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
            name='ProjectCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed_project_number', models.IntegerField(verbose_name='Completed Porject Number')),
                ('total_phases_number', models.IntegerField(verbose_name='Total Phase Number')),
                ('feedback_received_number', models.IntegerField(verbose_name='Feedback Received Number')),
                ('adiva_incurred_hours', models.IntegerField(verbose_name='Adiva Incurred Hours')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Company', verbose_name='Company Name')),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Months', verbose_name='Month')),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='projectcounter',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Year', verbose_name='Year'),
        ),
    ]
