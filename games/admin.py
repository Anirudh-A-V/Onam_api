from django.contrib import admin
from .models import Game, player, PlayedGame


# Register your models here.

admin.site.register(Game)
admin.site.register(player)
admin.site.register(PlayedGame)
