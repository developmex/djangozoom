# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 21:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoclase', '0006_auto_20170906_2112'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Meetings',
            new_name='Meeting',
        ),
    ]
