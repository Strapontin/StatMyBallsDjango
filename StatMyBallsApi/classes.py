from StatMyBallsApi import models
from django.core import serializers


class Contest:
    contest = ""

    blue_composition = ""
    yellow_composition = ""

    blue_score = -1
    yellow_score = -1

    def set_contest_details(self):
        team_color_blue = models.TeamColor.objects.filter(name="blue")[0]
        team_color_yellow = models.TeamColor.objects.filter(name="yellow")[0]

        team_blue = models.Team.objects.get(contest=self.contest, team_color=team_color_blue)
        self.blue_score = team_blue.score
        self.blue_composition = models.TeamComposition.objects.filter(team=team_blue)

        team_yellow = models.Team.objects.get(contest=self.contest, team_color=team_color_yellow)
        self.yellow_score = team_yellow.score
        self.yellow_composition = models.TeamComposition.objects.filter(team=team_yellow)
