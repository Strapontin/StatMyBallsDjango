from django.contrib import admin
from .models import Goal, GoalType, PlayerPosition

admin.site.register(Goal)
admin.site.register(GoalType)
admin.site.register(PlayerPosition)