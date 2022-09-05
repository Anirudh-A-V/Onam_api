from django.shortcuts import render
from .models import Game, player, PlayedGame

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import GameSerializer, PlayerSerializer, PlayedGameSerializer

games_list = Game.objects.all().order_by('name')

class player_list(APIView):
    
    def get(self, request):
        players = player.objects.all().order_by('score')
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class game_list(APIView):
    
    def get(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class played_list(APIView):
    
    def get(self, request):
        played = PlayedGame.objects.all().order_by('score')[:2]
        serializer = PlayedGameSerializer(played, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PlayedGameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)