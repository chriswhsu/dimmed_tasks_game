# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-30 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_auto_20160824_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameround',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
