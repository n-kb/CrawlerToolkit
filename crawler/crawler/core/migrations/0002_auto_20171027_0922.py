# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='last_crawled',
        ),
        migrations.AddField(
            model_name='feed',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='feed',
            name='last_time_crawled',
            field=models.DateTimeField(null=True),
        ),
    ]