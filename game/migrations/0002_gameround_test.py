# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-22 22:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameround',
            name='test',
            field=models.BooleanField(default=False),
        ),
    ]
