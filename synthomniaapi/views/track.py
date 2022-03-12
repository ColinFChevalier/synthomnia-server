from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from synthomniaapi.models import Track, Mood, Artist

class TrackView(ViewSet):

    def list(self, request):
        track = Track.objects.all()
        serializer = TrackSerializer(track, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        track = Track()
        track.title = request.data["title"]
        track.bandcampURL = request.data["bandcampURL"]

        mood = Mood.objects.get(pk=request.data["mood"])
        track.mood = mood
        
        artist = Artist.objects.get(pk=request.data["artist"])
        track.artist = artist

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'title', 'bandcampURL', 'mood', 'artist')