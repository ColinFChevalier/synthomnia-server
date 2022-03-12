from rest_framework import status
from rest_framework.decorators import action
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from synthomniaapi.models import Artist, SynthomniaUser
from django.contrib.auth.models import User

class ArtistView(ViewSet):

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

class AristSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'user', 'bio')