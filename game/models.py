from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.

class FakeUser(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# GamePlan is a setup of a Game with the appropriate TaskTypes sequence and question counts or durations.
class GamePlan(models.Model):
    code = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30)
    active = models.BooleanField(default=True)
    tasktype = models.ManyToManyField(TaskType, through="GamePlanTaskType")

    def __str__(self):
        return self.name


class GamePlanTaskType(models.Model):
    game_plan = models.ForeignKey(GamePlan)
    task_type = models.ForeignKey(TaskType)
    sequence = models.IntegerField()
    task_duration_seconds = models.IntegerField(null=True)
    user_defined_dim = models.BooleanField()
    dim_percent = models.FloatField(null=True, validators=[MaxValueValidator(99),
                                                           MinValueValidator(0)
                                                           ])


# GameRound is a instance of a GamePlan with tasks and users and scores stored within.
class GameRound(models.Model):
    game_plan = models.ForeignKey(GamePlan)
    date_time = models.DateTimeField()
    complete = models.BooleanField(default=False)


class GameRoundUser(models.Model):
    game_round = models.ForeignKey(GameRound)
    user = models.ForeignKey(User, null=True)
    fake_user = models.ForeignKey(FakeUser, null=True)
    game_round_task = models.ManyToManyField("GameRoundTask", through="GameRoundUserTask")

    class Meta:
        unique_together = [('game_round', 'user'),('game_round','fake_user')]


class GameRoundTask(models.Model):
    game_round = models.ForeignKey(GameRound)
    game_plan_task_type = models.ForeignKey(GamePlanTaskType)
    complete = models.BooleanField(default=False)
    game_round_user = models.ManyToManyField(GameRoundUser, through="GameRoundUserTask")


class GameRoundUserTask(models.Model):
    game_round_user = models.ForeignKey(GameRoundUser)
    game_round_task = models.ForeignKey(GameRoundTask)
    start_time = models.DateTimeField()
    dim_percent = models.FloatField()
    score = models.IntegerField(null=True)
    score_log = models.CharField(max_length=200, null=True)
    complete = models.BooleanField(default=False)

    class Meta:
        unique_together = ('game_round_user', 'game_round_task')

