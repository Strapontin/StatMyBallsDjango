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
    contest = models.Contest()
    contest.save()

    # Creating both teams in db before adding players
    team_color_blue = models.TeamColor.objects.get(name="blue")
    team_color_yellow = models.TeamColor.objects.get(name="yellow")

    team_blue = models.Team(contest=contest, team_color=team_color_blue)
    team_blue.save()
    team_yellow = models.Team(contest=contest, team_color=team_color_yellow)
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
    result = {'status': 200, 'url': f'/contest/{contest.id}'}

    return JsonResponse(result)


def contest(request, contest_id):
    contest = models.Contest.objects.get(pk=contest_id)

    return render(request, 'StatMyBallsApi/contest.html', {
        'player_list': player_list
    })
