import random
from statistics import mean

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
from game.routines import first_names, last_initials


class FakeUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=1)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


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
    tasktype = models.ManyToManyField(TaskType, through="GamePlanTask")

    def __str__(self):
        return self.name


class GamePlanTask(models.Model):
    game_plan = models.ForeignKey(GamePlan)
    task_type = models.ForeignKey(TaskType)
    sequence = models.IntegerField()
    task_duration_seconds = models.IntegerField(null=True)
    user_defined_dim = models.BooleanField()
    dim_percent = models.FloatField(blank=True, null=True, validators=[MaxValueValidator(99),
                                                                       MinValueValidator(0)
                                                                       ])


# GameRound is a instance of a GamePlan with tasks and users and scores stored within.
class GameRound(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    game_plan = models.ForeignKey(GamePlan)
    date_time = models.DateTimeField()
    complete = models.BooleanField(default=False)
    fake_user_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        super(GameRound, self).save(*args, **kwargs)  # Call the "real" save() method.

        uc = GameRoundUser.objects.filter(game_round=self, fake_user__isnull=False).count()

        if uc == self.fake_user_count:
            pass

        else:

            GameRoundUser.objects.filter(game_round=self, fake_user__isnull=False).delete()

            for x in range(self.fake_user_count):
                # create the appropriate number of fake users
                fu = FakeUser(first_name=random.choice(first_names), last_name=random.choice(last_initials))
                fu.save()

                # and fake GameRoundUsers
                grfu = GameRoundUser(fake_user=fu, game_round=self)
                grfu.save()


class GameRoundUser(models.Model):
    game_round = models.ForeignKey(GameRound)
    user = models.ForeignKey(User, null=True, blank=True)
    fake_user = models.ForeignKey(FakeUser, null=True, blank=True)
    game_round_task = models.ManyToManyField("GameRoundTask", through="GameRoundUserTask")

    class Meta:
        unique_together = [('game_round', 'user'), ('game_round', 'fake_user')]


class GameRoundTask(models.Model):
    game_round = models.ForeignKey(GameRound)
    game_plan_task = models.ForeignKey(GamePlanTask)
    complete = models.BooleanField(default=False)
    game_round_user = models.ManyToManyField(GameRoundUser, through="GameRoundUserTask")


class GameRoundUserTask(models.Model):
    game_round_user = models.ForeignKey(GameRoundUser)
    game_round_task = models.ForeignKey(GameRoundTask)
    start_time = models.DateTimeField(null=True)
    dim_percent = models.FloatField(null=True)
    score = models.IntegerField(null=True)
    score_log = models.CharField(max_length=200, null=True)
    complete = models.BooleanField(default=False)

    class Meta:
        unique_together = ('game_round_user', 'game_round_task')


# =========================================================================================================



def create_fake_users(game_round, user_count):
    uc = GameRoundUser.objects.filter(game_round=game_round, fake_user__isnull=False).count()

    if uc == user_count:
        pass

    else:

        for x in range(user_count):
            # create the appropriate number of fake users
            fu = FakeUser(first_name=random.choice(first_names), last_name=random.choice(last_initials))
            fu.save()

            # and fake GameRoundUsers
            grfu = GameRoundUser(fake_user=fu, game_round=game_round)
            grfu.save()


def derive_fake_user_dim(other_users_dim_percent):
    return round(random.triangular(max(min(other_users_dim_percent) - 10, 0),
                                   min(max(other_users_dim_percent) + 10, 95),
                                   mean(other_users_dim_percent)))


def derive_fake_user_score(other_users_score):
    return round(random.triangular(max(min(other_users_score) - 2, 0),
                                   max(other_users_score) + 1,
                                   mean(other_users_score)))


# create the tasks for a given game round based upon the task for the plan being executed.
def create_game_round_tasks(gp, gr):
    # get the tasks for a given game plan
    plan_tasks = GamePlanTask.objects.filter(game_plan=gp)

    for tk in plan_tasks:
        grt = GameRoundTask(game_round=gr, game_plan_task=tk)
        grt.save()

        # get users in this game_round

        users = GameRoundUser.objects.filter(game_round=gr)


def build_fake_grut_scores_and_dim(game_round_task):
    # get all the fake users
    game_round_users = GameRoundUser.objects.filter(game_round=game_round_task.game_round,
                                                    fake_user__isnull=False,
                                                    )

    game_round_user_tasks = GameRoundUserTask.objects.filter(game_round_task=game_round_task, game_round_user__fake_user__isnull=True)

    scores = []
    dims = []
    for grut in game_round_user_tasks:
        scores.append(grut.score)
        dims.append(grut.dim_percent)

    for gru in game_round_users:

        try:
            grut = GameRoundUserTask(game_round_user=gru,
                                     game_round_task=game_round_task,
                                     dim_percent=derive_fake_user_dim(dims),
                                     score=derive_fake_user_score(scores),
                                     complete=True)

            grut.save()
        except:
            pass


# This will check to see if the game round user tasks are complete and if so mark the game round task complete.
def check_for_round_task_complete(grt):
    complete = True

    gruts = GameRoundUserTask.objects.filter(game_round_task=grt, game_round_user__fake_user__isnull=True)

    gru_count = GameRoundUser.objects.filter(game_round=grt.game_round, fake_user__isnull=True).count()

    # don't have a task for each user yet.
    if gruts.count() < gru_count:
        complete = False

    for tk in gruts:
        if not tk.complete:
            complete = False

    if complete:
        grt.complete = True
        grt.save()
        return True
    else:
        return False


# This will check to see if the game round tasks are complete and if so mark the game round complete.
def check_for_round_complete(gr):
    complete = True

    grts = GameRoundTask.objects.filter(game_round=gr)

    for tk in grts:
        if not tk.complete:
            complete = False

    if complete:
        gr.complete = True
        gr.save()
        return True
    else:
        return False


def calculate_score(game_round_user):
    grut = GameRoundUserTask.objects.filter(game_round_user=game_round_user)
    score = 0
    for x in grut:
        score += x.score
    return score


def calculate_scaled_score(score, dim_percent):
    return dim_percent * score
