# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 12:06
from __future__ import unicode_literals

import crawler.core.resource_models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20171105_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='resource_file',
            field=models.FileField(max_length=255, upload_to=crawler.core.resource_models.resource_path),
        ),
    ]