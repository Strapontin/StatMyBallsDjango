from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Enum For Player position
class PlayerPosition(models.Model):
    position = models.CharField(max_length=60)

    def __str__(self):
        return self.position


# Enum For Goal Types
class GoalType(models.Model):
    label = models.CharField(max_length=60)

    def __str__(self):
        return self.label


# Model for Goals Table
class Goal(models.Model):
    goal_date = models.DateTimeField('goal_date', auto_now_add=True)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    player_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE)
    goal_type = models.ForeignKey(GoalType, on_delete=models.CASCADE)

    def __str__(self):
        template = '{0.player} a marqué {0.goal_type} depuis {0.player_position} à {0.goal_date}'
        return template.format(self)
