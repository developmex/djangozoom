# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoclase', '0002_auto_20170906_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoclase',
            name='meeting_id',
            field=models.CharField(max_length=42),
        ),
    ]