# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-24 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_fakeuser_game_round'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameroundusertask',
            name='dim_percent',
            field=models.FloatField(null=True),
        ),
    ]
