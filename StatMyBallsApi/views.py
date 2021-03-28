from django.shortcuts import render
from StatMyBallsApi.models import Player
from django.core import serializers
from django.http import JsonResponse
from StatMyBallsApi import models


# Create your views here.
def home(request):
    return render(request, 'StatMyBallsApi/home.html')


def create(request):
    player_list = serializers.serialize("python", Player.objects.order_by('name'))
    return render(request, 'StatMyBallsApi/create.html', {
        'player_list': player_list
    })


def start_contest(request):

    player_ids = request.GET.getlist("players[]")
    print(player_ids)

    contest_id = models.Contest().save().id

    # TODO Create contest with correct teams. Maybe change the Js part to know explicitly which player is in which team
    # TODO Then add player to the correct team

    result = {'status': 200, 'data': 'data'}
    return JsonResponse(result)
