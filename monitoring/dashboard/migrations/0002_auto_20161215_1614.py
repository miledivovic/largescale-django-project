# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-15 21:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='counter',
            old_name='node_id',
            new_name='node',
        ),
        migrations.RenameField(
            model_name='node',
            old_name='service_id',
            new_name='service',
        ),
    ]
