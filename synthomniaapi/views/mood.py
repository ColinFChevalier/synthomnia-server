from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from synthomniaapi.models import Mood, SynthomniaUser
from django.contrib.auth.models import User

class MoodView(ViewSet):

    def create(self, request):

        synthomniauser = SynthomniaUser.objects.get(user=request.auth.user)

        mood = Mood()
        mood.synthomniauser = synthomniauser
        mood.name = request.data["name"]
        mood.imgURL = request.data["imgURL"]

        try:
            mood.save()
            serializer = MoodSerializer(mood, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, pk=None):
            mood = Mood.objects.all()
            serializer = MoodSerializer(
                mood, many=True, context={'request': request})
            return Response(serializer.data)
            
    def retrieve(self, request, pk=None):
        try:
            mood = Mood.objects.get(pk=pk)
            serializer = MoodSerializer(mood, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        
        synthomniauser = SynthomniaUser.objects.get(user=request.auth.user)

        mood = Mood()
        mood.sythomniauser = synthomniauser
        mood.name = request.data["name"]
        mood.imgURL = request.data["imgURL"]
        mood.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            mood = Mood.objects.get(pk=pk)
            mood.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        
        except Mood.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class PostUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id']

# class MoodSynthomniaUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SynthomniaUser
#         fields = ['id']

class MoodSerializer(serializers.ModelSerializer):
    # synthomnia_user = MoodSynthomniaUserSerializer(many=False)
    class Meta:
        model = Mood
        fields = ('id', 'name', 'imgURL')