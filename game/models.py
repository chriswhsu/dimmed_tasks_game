from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class TaskType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# GamePlan is a setup of a Game with the appropriate TaskTypes sequence and question counts.

class GamePlan(models.Model):
    name = models.CharField(max_length=30)
    tasktype = models.ManyToManyField(TaskType, through="GamePlanTaskType")


class GamePlanTaskType(models.Model):
    gameplan = models.ForeignKey(GamePlan)
    tasktype = models.ForeignKey(TaskType)
    sequence = models.IntegerField()
    question_count = models.IntegerField()


# GameRound is a instance of a GamePlan with tasks and users and scores stored within.

class GameRound(models.Model):
    gameplan = models.ForeignKey(GamePlan)
    datetime = models.DateTimeField()


class GameRoundTask(models.Model):
    gameround = models.ForeignKey(GameRound)
    task_number = models.IntegerField()


class GameRoundTaskUser(models.Model):
    gameroundTask = models.ForeignKey(GameRoundTask)
    user = models.ForeignKey(User)
    dim_percent = models.FloatField()
    score = models.FloatField()
    points = models.IntegerField()

