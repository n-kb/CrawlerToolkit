# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20171103_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='url',
            field=models.URLField(db_index=True),
        ),
    ]
