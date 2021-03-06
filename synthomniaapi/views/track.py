from rest_framework import status
from rest_framework.decorators import action
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from synthomniaapi.models import Track, Mood, Artist

class TrackView(ViewSet):

    def list(self, request):
        track = Track.objects.all()
        mood = self.request.query_params.get("moodId", None)
        serializer = TrackSerializer(track, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            track = Track.objects.get(pk=pk)
            mood = Mood.objects.get(pk=request.data["moodId"])
            serializer = TrackSerializer(track, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)


    def create(self, request):
        track = Track()
        track.title = request.data["title"]
        track.bandcampURL = request.data["bandcampURL"]
        
        mood = Mood.objects.get(pk=request.data["mood"])
        track.mood = mood
        # artist = Artist.objects.get(pk=request.data["artist"])
        # track.artist = artist

        try:
            track.save()
            serializer = TrackSerializer(track, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
        
class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'title', 'bandcampURL', 'mood')