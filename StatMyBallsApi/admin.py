from django.contrib import admin
from .models import Goal, GoalType, Player

admin.site.register(Goal)
admin.site.register(GoalType)
admin.site.register(Player)
