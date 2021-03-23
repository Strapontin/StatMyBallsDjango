from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Should not be necessary
# # Enum For Player position
# class PlayerPosition(models.Model):
#     position = models.CharField(max_length=60)
#
#     def __str__(self):
#         return self.position

# Model for each context
class Contest(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = 'Démarré le {0.start_date}'
        return template.format(self)


# Enum for team colors
class TeamColor(models.Model):
    name = models.CharField(max_length=30)
    rgb_value = CharField(max_length=10)

    def __str__(self):
        return self.name


# Model for each team
class Team(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    team_color = models.ForeignKey(TeamColor, on_delete=models.CASCADE)

    def __str__(self):
        template = 'Equipe {0.team_color.name} du match démarré le {0.contest.start_date}'
        return template.format(self)


# Model for each player
class Player(models.Model):
    name = CharField(max_length=10)

    def __str__(self):
        return self.name


# Model to describe players in team
class TeamComposition(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        template = "Le joueur {0.player.name} est dans l'équipe {0.team.team_color}"
        return template.format(self)


# Enum For Goal Types
class GoalType(models.Model):
    label = models.CharField(max_length=60)

    def __str__(self):
        return self.label


# Model for Goals Table
class Goal(models.Model):
    goal_date = models.DateTimeField('goal_date', auto_now_add=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    # player_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE)
    goal_type = models.ForeignKey(GoalType, on_delete=models.CASCADE)
    enemy_player = models.ForeignKey(Player, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)

    def __str__(self):
        template = '{0.player} a marqué {0.goal_type} face à {0.enemy_player} à {0.goal_date}'
        return template.format(self)
