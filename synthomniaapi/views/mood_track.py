from rest_framework import status
from rest_framework.decorators import action
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from synthomniaapi.models import Track, Mood, Artist

class MoodTrackView(ViewSet):

    def list(self, request):
        # mood = Mood.objects.get(pk=request.data["mood"])
        mood = self.request.query_params.get("moodId", None)
        track = Track.objects.filter(mood = mood)
        serializer = TrackSerializer(track, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            # track = Track.objects.get(pk=pk)
            # import pdb; pdb.set_trace()
            mood = Mood.objects.get(pk=request.data["mood"])
            track = Track.objects.filter(mood = mood)
            serializer = TrackSerializer(track, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

class TrackMoodSerializer(serializers.ModelSerializer):
    # synthomnia_user = MoodSynthomniaUserSerializer(many=False)
    class Meta:
        model = Mood
        fields = ('id', 'name', 'imgURL')

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'title', 'bandcampURL', 'mood', 'artist')