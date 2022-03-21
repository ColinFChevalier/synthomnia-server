from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from synthomniaapi.models import SynthomniaUser
from django.http import HttpResponseServerError

class SynthomniaUserView(ViewSet):
    """
    viewset for SynthonmiaUser View
    """
    def list(self, request):
        synthomniauser = SynthomniaUser.objects.get(user=request.auth.user)
        # synthomniauser = SynthomniaUser.objects.all()

        synthomniauser = SynthomniaUserSerializer(
            synthomniauser, many=False, context={'request': request}
        )

        profile = {}
        # profile.user = request.data["user"]
        profile["synthomniauser"] = synthomniauser.data

        return Response(profile)

    def retrieve(self,request, pk=None):
        """Get request for single Comment"""
        
        try: 
            
            synthomniauser = SynthomniaUser.objects.get(pk=pk)
            serializer = SynthomniaUserSerializer(synthomniauser, context={'request': request })
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        synthomniauser = SynthomniaUser.objects.get(pk=pk)
        synthomniauser.bio = request.data["bio"]
        synthomniauser.profile_image_url = request.data["profile_image_url"]
        synthomniauser.save()
        
        return Response({}, status=status.HTTP_204_NO_CONTENT)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'is_superuser', 'is_staff')

class SynthomniaUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = SynthomniaUser
        fields = ('id', 'user', 'bio', 'profile_image_url',
        'created_on', 'active')






    # @action(methods=["GET"], detail=True)
    # def posts(self,request, pk=None):
    #     user_posts = Post.objects.filter(rare_user=pk)
    #     serializer = PostSerializer(user_posts, context={'request: request'}, many=True)
    #     return Response(serializer.data)