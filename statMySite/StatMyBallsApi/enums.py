from django.db import models
import enum

class PlayerPosition(models.Model):
    position_types = (
        (1, "Avant"),
        (2, "Defence"),
        (3, "Goal"),
    )
    position = models.IntegerField(choices=position_types, default=1)

