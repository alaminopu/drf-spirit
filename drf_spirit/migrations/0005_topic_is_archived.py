# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-25 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_spirit', '0004_auto_20170406_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ]
