import datetime
import logging

from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from game.models import GamePlan, GameRound, GameRoundUser
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

    now = datetime.datetime.now()
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
    username = request.user.username
    user = User.objects.get(username=username)



    return render(request, 'memory.html', {'show_user_dim': False,
                                           'dim_level': 0.6,
                                           'started':True})


