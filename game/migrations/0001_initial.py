# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-22 22:16
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FakeUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='GamePlan',
            fields=[
                ('code', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='GamePlanTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.IntegerField()),
                ('task_duration_seconds', models.IntegerField(null=True)),
                ('user_defined_dim', models.BooleanField()),
                ('dim_percent', models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)])),
                ('game_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.GamePlan')),
            ],
        ),
        migrations.CreateModel(
            name='GameRound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('complete', models.BooleanField(default=False)),
                ('game_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.GamePlan')),
            ],
        ),
        migrations.CreateModel(
            name='GameRoundTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete', models.BooleanField(default=False)),
                ('game_plan_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.GamePlanTask')),
                ('game_round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.GameRound')),
            ],
        ),
        migrations.CreateModel(
            name='GameRoundUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fake_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='game.FakeUser')),
                ('game_round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.GameRound')),
            ],
        ),
        migrations.CreateModel(
            name='GameRoundUserTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(null=True)),
                ('dim_percent', models.FloatField()),
                ('score', models.IntegerField(null=True)),
                ('score_log', models.CharField(max_length=200, null=True)),
                ('complete', models.BooleanField(default=False)),
                ('game_round_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.GameRoundTask')),
                ('game_round_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.GameRoundUser')),
            ],
        ),
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='gamerounduser',
            name='game_round_task',
            field=models.ManyToManyField(through='game.GameRoundUserTask', to='game.GameRoundTask'),
        ),
        migrations.AddField(
            model_name='gamerounduser',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gameroundtask',
            name='game_round_user',
            field=models.ManyToManyField(through='game.GameRoundUserTask', to='game.GameRoundUser'),
        ),
        migrations.AddField(
            model_name='gameplantask',
            name='task_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.TaskType'),
        ),
        migrations.AddField(
            model_name='gameplan',
            name='tasktype',
            field=models.ManyToManyField(through='game.GamePlanTask', to='game.TaskType'),
        ),
        migrations.AlterUniqueTogether(
            name='gameroundusertask',
            unique_together=set([('game_round_user', 'game_round_task')]),
        ),
        migrations.AlterUniqueTogether(
            name='gamerounduser',
            unique_together=set([('game_round', 'fake_user'), ('game_round', 'user')]),
        ),
    ]
