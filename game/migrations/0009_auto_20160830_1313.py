# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-30 20:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_gameround_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fakeuser',
            name='game_round',
        ),
        migrations.AlterField(
            model_name='gamerounduser',
            name='fake_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.FakeUser'),
        ),
        migrations.AlterField(
            model_name='gamerounduser',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
