import datetime
import json
import logging

from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import game.date_time_help as dth
from game.models import GamePlan, GameRound, GameRoundUser, GamePlanTaskType, GameRoundUserTask, GameRoundTask

# Create your views here.


from django.http import HttpResponse


# Game page
def index(request):
    game_plans = GamePlan.objects.filter(active=True)
    return render(request, "home.html", {'game_plans': game_plans})


def login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get("Email")
            password = request.POST.get("Password")
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                # Correct password, and the user is marked "active"
                auth.login(request, user)
                logging.info("Login success: user=%s" % username)
                return HttpResponseRedirect('/game/')
            else:
                return render(request, 'home.html', {'login': "false"})
        except:
            logging.info("Error! Received HTTP POST method, but data is wrong.")
            return HttpResponse("Error! Received HTTP POST method, but data is wrong.")
    else:
        logging.info("Error! Expecting  POST method!")
        return HttpResponse("Error! Expecting POST method!")


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return HttpResponseRedirect('/game/')
    else:
        logging.info("Error! Expecting  POST method!")
        return HttpResponse("Error! Expecting POST method!")


def run_game(request, plan):
    game_plan = GamePlan.objects.get(code=plan)

    username = request.user.username
    user = User.objects.get(username=username)

    now = dth.now_cur_tz()
    game_round = GameRound.objects.filter(complete=False, date_time__lte=now, date_time__gte=now - datetime.timedelta(hours=1))

    if not game_round:
        game_round = GameRound(date_time=now, game_plan=game_plan)
        game_round.save()
    else:
        game_round = game_round[0]

    game_round_user = GameRoundUser.objects.filter(game_round=game_round, user=user)

    if not game_round_user:
        game_round_user = GameRoundUser(game_round=game_round, user=user)
        game_round_user.save()
    else:
        game_round_user = game_round_user[0]

    user_count = GameRoundUser.objects.filter(game_round=game_round).count()

    return render(request, 'run_game.html', {'game_plan': game_plan,
                                             'game_round': game_round,
                                             'game_round_user': game_round_user,
                                             'user_count': user_count})


def start_game(request, game_round_user_id):
    # username = request.user.username
    # user = User.objects.get(username=username)

    gru = GameRoundUser.objects.get(pk=game_round_user_id)
    gr = GameRound.objects.get(gamerounduser=gru)

    gp = gr.game_plan

    # get the first task for this game round that doesn't have a task created.
    next_task = GamePlanTaskType.objects.filter(game_plan=gp,
                                                gameroundtask__isnull=True).order_by('sequence')[:1][0]

    # create the task for this game round if it doesn't exist
    grt, created = GameRoundTask.objects.get_or_create(game_round=gr,
                                                       game_plan_task_type=next_task
                                                       )
    grt.save()

    # create the user record for this game round task.
    grut, created = GameRoundUserTask.objects.get_or_create(game_round_user=gru,
                                                            game_round_task=grt,
                                                            defaults={'start_time': dth.now_cur_tz(), 'dim_percent': next_task.dim_percent})
    grut.save()

    return render(request, next_task.task_type.url, {'show_user_dim': next_task.user_defined_dim,
                                                     'dim_level': next_task.dim_percent / 100,
                                                     'started': True,
                                                     'grut': grut})


@csrf_exempt
def next_iteration_ajax(request):
    if request.is_ajax():
        if request.user.is_authenticated():
            if request.method == 'POST':
                try:
                    data = json.loads(request.body.decode())
                    user = User.objects.get(username=request.user.username)
                    clicks = data['clicks']

                    grut = GameRoundUserTask.objects.get(pk=data['grut_id'])

                    duration = grut.game_round_task.game_plan_task_type.task_duration_seconds

                    elapsed = (dth.now_cur_tz() - grut.start_time).total_seconds()

                    if elapsed > duration:
                        over = 1
                    else:
                        over = 0

                    if not grut.score:

                        grut.score = 1
                        grut.score_log = str(clicks)

                    else:
                        grut.score += 1
                        grut.score_log = grut.score_log + ',' + str(clicks)

                    grut.save()

                    results = {'success': True, 'score': grut.score, 'over': over}

                    json_res = json.dumps(results)



                except:
                    raise
                return HttpResponse(json_res, content_type='application/json')
            else:
                return HttpResponse("POST ONLY.")
        else:
            return HttpResponse("Authenticated usage only.")
    else:
        return HttpResponse("Only for ajax usage.")  # Function for page view log
