# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-14 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0025_gameround_winning_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameround',
            name='number_of_winners',
            field=models.IntegerField(default=1),
        ),
    ]
