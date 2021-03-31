from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import models
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from . import models
from django.utils import timezone
import datetime


def index(request):
    config = models.config.objects.get(id=1)
    # the level upto which questions is currently released.
    lastlevel = config.totallevel
    # the total no. of levels that would eventually be released.
    numlevel = config.numlevel
    countdown = config.countdown

    if request.user.is_authenticated:
        if countdown and (not request.user.is_staff):
            # if countdown:
            print(datetime.datetime.now())
            return render(request, 'timer.html', {'time': config.time})

        player = models.player.objects.get(user_id=request.user.pk)
        if player.current_level <= lastlevel:
            level = models.level.objects.get(l_number=player.current_level)
            return render(request, 'level.html', {'player': player, 'level': level})
        else:
            if player.current_level == numlevel + 1:
                return render(request, 'win.html', {'player': player})
            return render(request, 'finish.html', {'player': player})
    return render(request, 'index_page.html')


def save_profile(backend, user, response, *args, **kwargs):
    print(backend.name)
    print(response.items())
    if backend.name == 'github':
        profile = user
        try:
            player = models.player.objects.get(user=profile)
        except:
            player = models.player(user=profile)
            player.name = response.get('name')
            player.timestamp = datetime.datetime.now()
            player.profile_url = response.get('avatar_url')
            player.save()
    elif backend.name == 'google-oauth2':
        profile = user
        try:
            player = models.player.objects.get(user=profile)
        except:
            player = models.player(user=profile)
            player.timestamp = datetime.datetime.now()
            player.name = response.get('name')
            player.profile_url = response.get('picture')
            player.save()


@login_required
def answer(request):
    config = models.config.objects.get(id=1)
    lastlevel = config.totallevel
    numlevel = config.numlevel

    ans = ""
    level_answer = ""
    if request.method == 'POST':
        ans = request.POST.get('ans')
        ans = ans.replace(" ", "").lower()

    player = models.player.objects.get(user_id=request.user.pk)
    if player.current_level <= lastlevel:
        level = models.level.objects.get(l_number=player.current_level)
    else:
        if player.current_level == numlevel + 1:
            return render(request, 'win.html', {'player': player})
        return render(request, 'finish.html', {'player': player})

    if ans == level.answer.replace(" ", "").lower():
        player.current_level = player.current_level + 1
        player.score = player.score + 10
        player.timestamp = datetime.datetime.now(tz=timezone.utc)
        level.numuser = level.numuser + 1
        level.accuracy = round(
            level.numuser/(float(level.numuser + level.wrong)), 2)
        level.save()
        player.save()
        if player.current_level <= lastlevel:
            level = models.level.objects.get(l_number=player.current_level)
            return render(request, 'level_transition.html')
        else:
            if player.current_level == numlevel + 1:
                return render(request, 'win.html', {'player': player})
            return render(request, 'finish.html', {'player': player})

    elif ans == "":
        if request.method == "POST":
            messages.error(request, "Please enter an answer!")
        return render(request, 'level.html', {'player': player, 'level': level})

    else:
        level.wrong = level.wrong + 1
        level.save()

        messages.error(request, "Wrong Answer!, Try Again")

    return render(request, 'level.html', {'player': player, 'level': level})


def lboard(request):
    players = models.player.objects.order_by('-score', 'timestamp')
    if request.user.is_authenticated:
        player = models.player.objects.get(user_id=request.user.pk)
    cur_rank = 1

    for pl in players:
        pl.rank = cur_rank
        cur_rank += 1

    first = players[0]
    second = players[1]
    third = players[2]

    if len(players) > 3:
        players = players[3:]
    else:
        players = []
    print(first, second, third)
    if request.user.is_authenticated:
        return render(request, 'lboard.html', {'players': players, 'player': player, 'first': first, 'second': second, 'third': third, 'hide': True})
    else:
        return render(request, 'lboard.html', {'players': players, 'first': first, 'second': second, 'third': third, 'hide': True})


def rules(request):
    if request.user.is_authenticated:
        player = models.player.objects.get(user_id=request.user.pk)
        return render(request, 'index_page.html', {'player': player})
    else:
        return render(request, 'index_page.html',)


def lboard_api(request):
    p = models.player.objects.order_by('-score', 'timestamp')
    cur_rank = 1
    for pl in p:
        pl.rank = cur_rank
        cur_rank += 1

    leaderboard = list()
    for pl in p:
        leaderboard.append({
            'rank': pl.rank,
            'name': pl.name,
            'email': pl.user.email,
            'score': pl.score,
        })

    return JsonResponse(leaderboard, safe=False)
