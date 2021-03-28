from django.db import models


# Model for each context
class Contest(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    def __str__(self):
        template = 'Démarré le {0.start_date}'
        return template.format(self)


# Enum for team colors
class TeamColor(models.Model):
    name = models.CharField(max_length=30)
    rgb_value = models.CharField(max_length=10)

    def __str__(self):
        return self.name


def init_team_color():
    if not TeamColor.objects.filter(name="yellow").exists():
        TeamColor(name="yellow", rgb_value="#FFFF00").save()

    if not TeamColor.objects.filter(name="blue").exists():
        TeamColor(name="blue", rgb_value="#0000FF").save()


# Model for each team
class Team(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    team_color = models.ForeignKey(TeamColor, on_delete=models.CASCADE)

    def __str__(self):
        template = 'Equipe {0.team_color.name} du match démarré le {0.contest.start_date}'
        return template.format(self)


# Model for each player
class Player(models.Model):
    name = models.CharField(max_length=10)

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
    is_from_defense = models.BooleanField()

    def __str__(self):
        return self.label


# Model for Gvoals Table
class Goal(models.Model):
    goal_date = models.DateTimeField('goal_date', auto_now_add=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='%(class)s_player_scored')
    enemy_player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='%(class)s_enemy_player')
    goal_type = models.ForeignKey(GoalType, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    is_bounce_out = models.BooleanField()

    def __str__(self):
        template = '{0.player} a marqué {0.goal_type} face à {0.enemy_player} à {0.goal_date}'
        return template.format(self)
