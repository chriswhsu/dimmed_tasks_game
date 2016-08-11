from game.models import GamePlanTask, GameRoundUserTask, GameRoundTask


# create the tasks for a given game round based upon the task for the plan being executed.
def create_game_round_tasks(gp, gr):
    # get the tasks for a given game plan
    plan_tasks = GamePlanTask.objects.filter(game_plan=gp)

    for tk in plan_tasks:
        grt = GameRoundTask(game_round=gr, game_plan_task=tk)
        grt.save()


# This will check to see if the game round user tasks are complete and if so mark the game round task complete.
def check_for_round_task_complete(grt):
    complete = True

    gruts = GameRoundUserTask.objects.filter(game_round_task=grt)

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
