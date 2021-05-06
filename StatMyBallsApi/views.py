from django.shortcuts import render
from StatMyBallsApi.models import Player
from django.core import serializers
from django.http import JsonResponse
from StatMyBallsApi import models
import json


# Create your views here.
def home(request):
    return render(request, 'StatMyBallsApi/home.html')


def create(request):
    player_list = serializers.serialize("python", Player.objects.order_by('name'))
    return render(request, 'StatMyBallsApi/create.html', {
        'player_list': player_list
    })


def start_contest(request):
    player_teams = request.GET.getlist("player_teams[]")

    # Creating a new match
    current_contest = models.Contest()
    current_contest.save()

    # Creating both teams in db before adding players
    team_color_blue = models.TeamColor.objects.get(name="blue")
    team_color_yellow = models.TeamColor.objects.get(name="yellow")

    team_blue = models.Team(contest=current_contest, team_color=team_color_blue)
    team_blue.save()
    team_yellow = models.Team(contest=current_contest, team_color=team_color_yellow)
    team_yellow.save()

    # Adding players to teams
    for team in player_teams:
        team = json.loads(team)

        # Get the player instance
        player = models.Player(id=team['player'])

        if team['color'] == "blue":
            team_to_join = team_blue
        else:
            team_to_join = team_blue
        models.TeamComposition(team=team_to_join, player=player).save()

    # Teams are created, now we redirect the user to the contest page
    result = {'status': 200, 'url': f'/contest/{current_contest.id}'}

    return JsonResponse(result)


def contest(request, contest_id):
    current_contest = models.Contest.objects.get(pk=contest_id)

    print(current_contest)

    goal_types = serializers.serialize("python", models.GoalType.objects.all())

    return render(request, 'StatMyBallsApi/contest.html', {
        'contest': current_contest,
        'goal_types': goal_types
    })


class Contest:
    contest = ""
    team = ""


def all_contests(request):
    all_contest = []

    for contest in models.Contest.objects.all():
        c = Contest()
        c.contest = contest
        c.team = models.Team.objects.filter(contest=contest)

        all_contest.append(c)

    print(all_contest)

    # contests = serializers.serialize("python", my_contest)

    return render(request, 'StatMyBallsApi/all_contests.html', {
        'contests': all_contest,
    })
