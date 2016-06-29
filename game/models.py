from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TaskType(models.Model):
    name = models.CharField(max_length=30)


class GameRound(models.Model):
    datetime = models.DateTimeField()
    users = models.ManyToManyField(User, through="GameRoundUser")
    tasktype = models.ManyToManyField(TaskType, through="GameRoundTaskType")


class GameRoundUser(models.Model):
    gameround = models.ForeignKey(GameRound)
    user = models.ForeignKey(User)
    name = models.CharField(max_length=30)
    occupation = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=50)
    sex = models.CharField(max_length=1)


class GameRoundTaskType(models.Model):
    gameround = models.ForeignKey(GameRound)
    tasktype = models.ForeignKey(TaskType)
    relative_weight = models.IntegerField()