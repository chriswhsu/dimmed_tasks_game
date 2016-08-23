import random

from game.models import GameRoundUser, GamePlanTask, GameRoundUserTask, GameRoundTask

first_names = [
    'Oliver'
    , 'Isabella'
    , 'Aiden'
    , 'Charlotte'
    , 'Elijah'
    , 'Harper'
    , 'James'
    , 'Amelia'
    , 'Benjamin'
    , 'Abigail'
    , 'Logan'
    , 'Emily'
    , 'Jacob'
    , 'Madison'
    , 'Jackson'
    , 'Lily'
    , 'Michael'
    , 'Ella'
    , 'Alexander'
    , 'Avery'
    , 'Luke'
    , 'Evelyn'
    , 'Carter'
    , 'Sofia'
    , 'Jack'
    , 'Aria'
    , 'Owen'
    , 'Chloe'
    , 'William'
    , 'Riley'
    , 'Daniel'
    , 'Ellie'
    , 'Gabriel'
    , 'Scarlett'
    , 'Henry'
    , 'Elizabeth'
    , 'Matthew'
    , 'Aubrey'
    , 'Wyatt'
    , 'Addison'
    , 'Sebastian'
    , 'Layla'
    , 'Nathan'
    , 'Grace'
    , 'Ryan'
    , 'Zoey'
    , 'Grayson'
    , 'Hannah'
    , 'Isaac'
    , 'Zoe'
    , 'Caleb'
    , 'Mila'
    , 'Jayden'
    , 'Brooklyn'
    , 'Levi'
    , 'Victoria'
    , 'David'
    , 'Nora'
    , 'Eli'
    , 'Lucy'
    , 'Dylan'
    , 'Natalie'
    , 'Jaxon'
    , 'Audrey'
    , 'Samuel'
    , 'Penelope'
    , 'Andrew'
    , 'Claire'
    , 'Julian'
    , 'Skylar'
    , 'John'
    , 'Robert'
    , 'Michael'
    , 'William'
    , 'David'
    , 'Richard'
    , 'Joseph'
    , 'Thomas'
    , 'Charles'
    , 'Christopher'
    , 'Daniel'
    , 'Matthew'
    , 'Anthony'
    , 'Donald'
    , 'Mark'
    , 'Paul'
    , 'Steven'
    , 'George'
    , 'Kenneth'
    , 'Andrew'
    , 'Joshua'
    , 'Edward'
    , 'Brian'
    , 'Kevin'
    , 'Ronald'
    , 'Timothy'
    , 'Jason'
    , 'Jeffrey'
    , 'Ryan'
    , 'Gary'
    , 'Jacob'
    , 'Nicholas'
    , 'Eric'
    , 'Stephen'
    , 'Jonathan'
    , 'Larry'
    , 'Scott'
    , 'Frank'
    , 'Justin'
    , 'Brandon'
    , 'Raymond'
    , 'Gregory'
    , 'Samuel'
    , 'Benjamin'
    , 'Patrick'
    , 'Jack'
    , 'Alexander'
    , 'Dennis'
    , 'Jerry'
    , 'Tyler'
    , 'Aaron'
    , 'Henry'
    , 'Douglas'
    , 'Peter'
    , 'Jose'
    , 'Adam'
    , 'Zachary'
    , 'Walter'
    , 'Nathan'
    , 'Harold'
    , 'Kyle'
    , 'Carl'
    , 'Arthur'
    , 'Gerald'
    , 'Roger'
    , 'Keith'
    , 'Jeremy'
    , 'Lawrence'
    , 'Terry'
    , 'Sean'
    , 'Albert'
    , 'Joe'
    , 'Christian'
    , 'Austin'
    , 'Willie'
    , 'Jesse'
    , 'Ethan'
    , 'Billy'
    , 'Bruce'
    , 'Bryan'
    , 'Ralph'
    , 'Roy'
    , 'Jordan'
    , 'Eugene'
    , 'Wayne'
    , 'Louis'
    , 'Dylan'
    , 'Alan'
    , 'Juan'
    , 'Noah'
    , 'Russell'
    , 'Harry'
    , 'Randy'
    , 'Philip'
    , 'Vincent'
    , 'Gabriel'
    , 'Bobby'
    , 'Johnny'
    , 'Howard'
    , 'Patricia'
    , 'Jennifer'
    , 'Elizabeth'
    , 'Linda'
    , 'Barbara'
    , 'Susan'
    , 'Jessica'
    , 'Margaret'
    , 'Sarah'
    , 'Karen'
    , 'Nancy'
    , 'Betty'
    , 'Dorothy'
    , 'Lisa'
    , 'Sandra'
    , 'Ashley'
    , 'Kimberly'
    , 'Donna'
    , 'Carol'
    , 'Michelle'
    , 'Emily'
    , 'Helen'
    , 'Amanda'
    , 'Melissa'
    , 'Deborah'
    , 'Stephanie'
    , 'Laura'
    , 'Rebecca'
    , 'Sharon'
    , 'Cynthia'
    , 'Kathleen'
    , 'Shirley'
    , 'Amy'
    , 'Anna'
    , 'Angela'
    , 'Ruth'
    , 'Brenda'
    , 'Pamela'
    , 'Virginia'
    , 'Katherine'
    , 'Nicole'
    , 'Catherine'
    , 'Christine'
    , 'Samantha'
    , 'Debra'
    , 'Janet'
    , 'Carolyn'
    , 'Rachel'
    , 'Heather'
    , 'Maria'
    , 'Diane'
    , 'Emma'
    , 'Julie'
    , 'Joyce'
    , 'Frances'
    , 'Evelyn'
    , 'Joan'
    , 'Christina'
    , 'Kelly'
    , 'Martha'
    , 'Lauren'
    , 'Victoria'
    , 'Judith'
    , 'Cheryl'
    , 'Megan'
    , 'Alice'
    , 'Ann'
    , 'Jean'
    , 'Doris'
    , 'Andrea'
    , 'Marie'
    , 'Kathryn'
    , 'Jacqueline'
    , 'Gloria'
    , 'Teresa'
    , 'Hannah'
    , 'Sara'
    , 'Janice'
    , 'Julia'
    , 'Olivia'
    , 'Grace'
    , 'Rose'
    , 'Theresa'
    , 'Judy'
    , 'Beverly'
    , 'Denise'
    , 'Marilyn'
    , 'Amber'
    , 'Danielle'
    , 'Brittany'
    , 'Madison'
    , 'Diana'
    , 'Jane'
    , 'Lori'
    , 'Mildred'
    , 'Tiffany'
    , 'Natalie'
    , 'Abigail'
    , 'Kathy'
]

last_initials = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'Y']


def random_first_last():
    return random.choice(first_names) + ' ' + random.choice(last_initials) + '.'


# create the tasks for a given game round based upon the task for the plan being executed.
def create_game_round_tasks(gp, gr):
    # get the tasks for a given game plan
    plan_tasks = GamePlanTask.objects.filter(game_plan=gp)

    for tk in plan_tasks:
        grt = GameRoundTask(game_round=gr, game_plan_task=tk)
        grt.save()

        # get users in this game_round

        users = GameRoundUser.objects.filter(game_round=gr)


# This will check to see if the game round user tasks are complete and if so mark the game round task complete.
def check_for_round_task_complete(grt):
    complete = True

    gruts = GameRoundUserTask.objects.filter(game_round_task=grt)

    gru_count = GameRoundUser.objects.filter(game_round=grt.game_round).count()

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
