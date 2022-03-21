from rest_framework import status
from rest_framework.decorators import action
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from synthomniaapi.models import Artist, SynthomniaUser, Mood
# from synthomniaapi.views.mood import MoodSerializer
from django.contrib.auth.models import User

class ArtistView(ViewSet):

    def list(self, request, pk=None):
            artist = Artist.objects.all()
            serializer = ArtistSerializer(
                artist, many=True, context={'request': request})
            return Response(serializer.data)
            
    def retrieve(self, request, pk=None):
        try:
            artist = Artist.objects.get(pk=pk)
            serializer = ArtistSerializer(artist, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def create(self, request):
        synthomniauser = SynthomniaUser.objects.get(user=request.auth.user)

        artist = Artist()
        artist.synthomniauser = synthomniauser
        artist.bio = request.data["bio"]

        try:
            artist.save()
            serializer = ArtistUserSerializer
            return Response(serializer.data)

        except Exception as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

class ArtistUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']

class ArtistMoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ('id', 'name', 'imgURL')

class ArtistSerializer(serializers.ModelSerializer):
    mood = ArtistMoodSerializer(many=True)
    class Meta:
        model = Artist
        fields = ('id', 'user', 'bio', 'mood')