# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-30 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_auto_20160830_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameplan',
            name='fake_user_count',
        ),
        migrations.AddField(
            model_name='gameround',
            name='fake_user_count',
            field=models.IntegerField(default=0),
        ),
    ]