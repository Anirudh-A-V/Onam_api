from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    played = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def getname(self):
        return self.name
    
    def getdescription(self):
        return self.description
    
    def getupdate(self):
        return self.updated_at
    
    def __str__(self):
        return self.name
    
class player(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    game_name = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    score = models.IntegerField(null=True)
    
    def __str__(self):
        return self.first_name + " " + self.last_name


class PlayedGame(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(player, on_delete=models.CASCADE)
    score = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.game.name + " played by " + self.player.first_name