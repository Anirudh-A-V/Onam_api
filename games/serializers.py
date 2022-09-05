from rest_framework import serializers
from .models import Game, player, PlayedGame

class GameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Game
        fields = ('id', 'name', 'description', 'updated_at')
        
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = player
        fields = ('id', 'first_name', 'last_name', 'score')
        
class PlayedGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayedGame
        fields = ('id', 'game', 'player', 'score', 'updated_at')