# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-31 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_auto_20160830_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameroundtask',
            name='sequence',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gameroundusertask',
            name='sequence',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
