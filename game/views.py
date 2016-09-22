import json
import logging
from collections import OrderedDict

from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models import Avg
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import game.date_time_help as dth
import game.models as md
from game.models import GameRound, GameRoundUser, GameRoundUserTask, GameRoundTask, QuestionChoice, GameRoundTaskQuestion, PrivacyChoice


# Game page
def index(request):
    if request.user.is_authenticated():

        username = request.user.username
        user = User.objects.get(username=username)

        game_rounds = GameRound.objects.filter(complete=False, gamerounduser__user=user)
        return render(request, "active_game_rounds.html", {'game_rounds': game_rounds})

    else:
        return render(request, "active_game_rounds.html", {})


def select_privacy(request, game_round_id):
    gr = GameRound.objects.get(pk=game_round_id)
    choices = PrivacyChoice.objects.all()

    return render(request, "privacy.html", {'game_round': gr, 'choices': choices})


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
                return render(request, 'active_game_rounds.html', {'login': "false"})
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


def run_game(request, game_round_id, continued=False):
    game_round = GameRound.objects.get(pk=game_round_id)

    username = request.user.username
    user = User.objects.get(username=username)

    privacy_choice_id = request.POST.get('choice')

    game_round_user, created = GameRoundUser.objects.get_or_create(game_round=game_round, user=user)
    game_round_user.privacy_choice = PrivacyChoice.objects.get(pk=privacy_choice_id)
    game_round_user.save()

    user_count = GameRoundUser.objects.filter(game_round=game_round).count()

    return render(request, 'run_game.html', {'continued': continued,
                                             'game_plan': game_round.game_plan,
                                             'game_round': game_round,
                                             'game_round_user': game_round_user,
                                             'user_count': user_count})


def start_game(request, game_round_user_id):
    # username = request.user.username
    # user = User.objects.get(username=username)

    gru = GameRoundUser.objects.get(pk=game_round_user_id)
    game_round = GameRound.objects.get(gamerounduser=gru)

    # get the first task for this game round that is incomplete.
    grt = GameRoundTask.objects.filter(game_round_id=game_round.id,
                                       complete=False,
                                       game_round__complete=False).order_by('game_plan_task__sequence')[:1][0]

    # create the user record for this game round task.
    grut, created = GameRoundUserTask.objects.get_or_create(game_round_user=gru,
                                                            game_round_task=grt,
                                                            sequence=grt.sequence,
                                                            defaults={'brightness': grt.game_plan_task.brightness})
    grut.save()

    if not grt.game_plan_task.brightness:
        brightness = 100
    else:
        brightness = grt.game_plan_task.brightness

    # check to see if all users in this game round have completed the prior task

    return render(request, 'run_game.html', {'show_user_brightness': grt.game_plan_task.user_defined_brightness,
                                             'brightness': brightness,
                                             'started': True,
                                             'game_round_user_task': grut,
                                             'brightness_level': brightness / 100})


def get_going(request, game_round_user_task_id, brightness):
    # username = request.user.username
    # user = User.objects.get(username=username)

    # Update with start time and brightness.
    grut = GameRoundUserTask.objects.get(pk=game_round_user_task_id)

    if not grut.start_time:
        grut.start_time = dth.now_cur_tz()
    grut.brightness = float(brightness)
    grut.save()

    # check to see if all users in this game round have completed the prior task

    if grut.game_round_task.game_plan_task.task_type.name == 'MultipleChoice':

        grtq = GameRoundTaskQuestion.objects.get(game_round_task=grut.game_round_task, question_sequence=1)

        return render(request, grut.game_round_task.game_plan_task.task_type.url, {
            'seconds_left': max(grut.game_round_task.game_plan_task.task_duration_seconds - (dth.now_cur_tz() - grut.start_time).total_seconds(), 0),
            'brightness_level': grut.brightness / 100,
            'started': True,
            'active_game_play': True,
            'game_round_user_task': grut,
            'question': grtq.question,
            'question_choices': grtq.question.questionchoice_set.all()
        })

    else:

        return render(request, grut.game_round_task.game_plan_task.task_type.url, {
            'seconds_left': max(grut.game_round_task.game_plan_task.task_duration_seconds - (dth.now_cur_tz() - grut.start_time).total_seconds(), 0),
            'brightness_level': grut.brightness / 100,
            'started': True,
            'active_game_play': True,
            'game_round_user_task': grut, })


def continue_game(request, game_round_user_task_id):
    # username = request.user.username
    # user = User.objects.get(username=username)

    grut = GameRoundUserTask.objects.get(id=game_round_user_task_id)

    grt = grut.game_round_task

    gru = grut.game_round_user

    gr = gru.game_round

    gp = gr.game_plan

    everyone_done_with_task = md.check_for_round_task_complete(grut.game_round_task)

    round_done = md.check_for_round_complete(gr)

    if not round_done:
        # get the first task for this game round that is incomplete.
        next_grt = GameRoundTask.objects.filter(game_round_id=gr.id,
                                                complete=False,
                                                game_round__complete=False).order_by('game_plan_task__sequence')[:1][0]

        if everyone_done_with_task:

            user_count = GameRoundUser.objects.filter(game_round=gr).count()

            md.build_fake_grut_scores_and_brightness(grt)

            return render(request, 'run_game.html', {'continued': True,
                                                     'game_plan': gp,
                                                     'game_round': gr,
                                                     'game_round_user': gru,
                                                     'game_round_task': grt,
                                                     'game_round_user_task': grut,
                                                     'active_game_play': False,
                                                     'user_count': user_count})

        else:
            return render(request, 'wait.html', {'started': True,
                                                 'brightness_level': 100,
                                                 'game_plan': gp,
                                                 'game_round': gr,
                                                 'game_round_user': gru,
                                                 'game_round_task': grt,
                                                 'game_round_user_task': grut,
                                                 'active_game_play': False})
    else:

        md.build_fake_grut_scores_and_brightness(grt)

        return render(request, 'round_over.html', {'game_plan': gp,
                                                   'game_round': gr,
                                                   'game_round_user': gru,
                                                   'game_round_task': grt,
                                                   'game_round_user_task': grut,
                                                   'active_game_play': False})


# This is used by single interation games like tetris and 2048.
@csrf_exempt
def send_score_ajax(request):
    if request.is_ajax():
        if request.user.is_authenticated():
            if request.method == 'POST':
                try:
                    data = json.loads(request.body.decode())
                    grut = GameRoundUserTask.objects.get(pk=data['grut_id'])

                    grut.complete = True
                    grut.score = data['score']
                    grut.save()

                    md.check_for_round_task_complete(grut.game_round_task)
                    md.check_for_round_complete(grut.game_round_task.game_round)

                    results = {'success': True, 'score': grut.score, 'over': True}

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


# This is only used by the Multiple Choice Game
@csrf_exempt
def get_question_and_choices_ajax(request):
    if request.is_ajax():
        if request.user.is_authenticated():
            if request.method == 'POST':
                try:
                    data = json.loads(request.body.decode())

                    grut = GameRoundUserTask.objects.get(pk=data['grut_id'])

                    question_id = data['question_id']
                    answer_code = ''
                    try:
                        answer_code = data['answer_code']
                    except KeyError:
                        pass

                    grtq_sequence = GameRoundTaskQuestion.objects.get(question_id=question_id, game_round_task=grut.game_round_task).question_sequence

                    if answer_code:

                        correct = QuestionChoice.objects.filter(question_id=question_id, choice_code=answer_code, correct_choice=True).count()
                    else:
                        correct = 0

                    duration = grut.game_round_task.game_plan_task.task_duration_seconds

                    elapsed = (dth.now_cur_tz() - grut.start_time).total_seconds()

                    if elapsed > duration:
                        over = 1
                        grut.complete = True
                    else:
                        over = 0
                        grut.complete = False

                    # only count correct answers towards score.
                    if not grut.score:

                        grut.score = correct * 100

                    else:
                        grut.score += correct * 100

                    grut.save()

                    if over:
                        md.check_for_round_task_complete(grut.game_round_task)
                        md.check_for_round_complete(grut.game_round_task.game_round)

                        results = {'success': True, 'score': grut.score, 'over': over}
                    else:
                        # get next question for this task.
                        grtq = GameRoundTaskQuestion.objects.get(game_round_task=grut.game_round_task, question_sequence=grtq_sequence + 1)

                        choice_list = []

                        for choice in grtq.question.questionchoice_set.all():
                            choice_list.append({'choice_text': choice.choice_text, 'choice_code': choice.choice_code})

                        results = {'success': True, 'score': grut.score, 'over': over, "question_id": grtq.question_id, "question_text": grtq.question.question_text, "choices": choice_list}

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


# This is only used by the memory game.
@csrf_exempt
def next_memory_iteration_ajax(request):
    if request.is_ajax():
        if request.user.is_authenticated():
            if request.method == 'POST':
                try:
                    data = json.loads(request.body.decode())

                    clicks = data['clicks']

                    if clicks == -1:
                        it_score = 0
                    else:
                        it_score = 100

                    grut = GameRoundUserTask.objects.get(pk=data['grut_id'])

                    duration = grut.game_round_task.game_plan_task.task_duration_seconds

                    elapsed = (dth.now_cur_tz() - grut.start_time).total_seconds()

                    if elapsed > duration:
                        over = 1
                        grut.complete = True
                    else:
                        over = 0
                        grut.complete = False

                    if not grut.score:
                        # Thousand points per correct answer
                        grut.score = it_score
                    else:
                        grut.score += it_score

                    grut.save()

                    md.check_for_round_task_complete(grut.game_round_task)
                    md.check_for_round_complete(grut.game_round_task.game_round)

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


@csrf_exempt
def get_comparison_points_ajax(request):
    if request.is_ajax():
        if request.user.is_authenticated():
            if request.method == 'POST':

                string = request.body.decode("utf-8")
                data = json.loads(string)
                grt_id = data['game_round_task_id']

                grt = GameRoundTask.objects.get(pk=grt_id)
                all_gru = GameRoundUser.objects.filter(game_round=grt.game_round)

                username = request.user.username

                user_points = dict()
                # get all users for the game round
                for gru in all_gru:
                    scaled_score = 0

                    # get all game round tasks for the user
                    gruts = GameRoundUserTask.objects.filter(game_round_user=gru, complete=True)

                    for game_round_user_task in gruts:
                        scaled_score += md.calculate_scaled_score(game_round_user_task.score, game_round_user_task.brightness)

                    if game_round_user_task.game_round_user.user:
                        if game_round_user_task.game_round_user.user.username == username:
                            its_me = True
                        else:
                            its_me = False
                    else:
                        its_me = False

                    uname = md.get_display_name(game_round_user_task.game_round_user)

                    user_points[uname] = [its_me,
                                          scaled_score,
                                          game_round_user_task.brightness]

                # sort the dictionary by point score.
                sorted_user_points = OrderedDict(sorted(user_points.items(), key=lambda e: e[1][1]))

                json_response = json.dumps(sorted_user_points)
                return HttpResponse(json_response, content_type='application/json')
        else:
            return HttpResponse("Authenticated usage only.")
    else:
        return HttpResponse("Only for ajax usage.")


def ordinal(n):
    if 10 <= n % 100 < 20:
        return str(n) + 'th'
    else:
        return str(n) + {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, "th")


@csrf_exempt
def get_summary_points_ajax(request):
    if request.is_ajax():
        if request.user.is_authenticated():
            if request.method == 'POST':

                string = request.body.decode("utf-8")
                data = json.loads(string)
                gr_id = data['game_round_id']

                gr = GameRound.objects.get(pk=gr_id)

                all_gru = GameRoundUser.objects.filter(game_round=gr)

                username = request.user.username
                user = User.objects.get(username=username)

                user_points = dict()

                winning_grus = md.determine_winners(game_round=gr)

                for game_round_user in all_gru:

                    scaled_score = 0

                    for grut in GameRoundUserTask.objects.filter(game_round_user=game_round_user):
                        scaled_score += md.calculate_scaled_score(grut.score, grut.brightness)

                    brightness = round(GameRoundUserTask.objects.filter(game_round_user=game_round_user).aggregate(Avg('brightness'))["brightness__avg"], 1)

                    if game_round_user.user:
                        if game_round_user.user.username == username:
                            its_me = True
                        else:
                            its_me = False

                    else:
                        its_me = False

                    uname = md.get_display_name(game_round_user)

                    user_points[uname] = [its_me,
                                          scaled_score,
                                          brightness,
                                          game_round_user.id in winning_grus]

                winning_text = ''

                for idx, gru in enumerate(winning_grus):
                    winning_text += ordinal(idx + 1) + ' Place: ' + md.get_display_name(GameRoundUser.objects.get(pk=gru)) + '<br />'

                results = {'points': user_points, 'winners_text': winning_text}

                json_response = json.dumps(results)
                return HttpResponse(json_response, content_type='application/json')
        else:
            return HttpResponse("Authenticated usage only.")
    else:
        return HttpResponse("Only for ajax usage.")
