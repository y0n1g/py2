from django.contrib import admin

# Register your models here.
from .models import Team, Player

class PlayerAdmin(admin.ModelAdmin):
    model = Player


class TeamAdmin(admin.ModelAdmin):
    model = Team


admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)

