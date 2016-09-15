# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-14 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0024_auto_20160914_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameround',
            name='winning_users',
            field=models.ManyToManyField(through='game.Winner', to='game.GameRoundUser'),
        ),
    ]
