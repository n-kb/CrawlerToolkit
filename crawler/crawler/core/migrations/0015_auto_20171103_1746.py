# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 17:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_fontresource'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StyeResource',
            new_name='StyleResource',
        ),
    ]
