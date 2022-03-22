from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.core.management import call_command
from django.contrib.auth.models import User

from synthomniaapi.models import Mood

class MoodTests(APITestCase):
    def setUp(self):
        """
        Seed the database
        """
        call_command('seed_db', user_count=3)
        self.user1 = User.objects.filter(store=None).first()
        self.token = Token.objects.get(user=self.user1)

        self.user2 = User.objects.filter(store=None).last()
        mood = Mood.objects.get(pk=1)

        self.order1 = Mood.objects.create(
            user=self.user1
        )

        self.order1.moods.add(mood)

        self.order2 = Mood.objects.create(
            user=self.user2
        )

        self.order2.products.add(mood)

        self.client.credentials(
            HTTP_AUTHORIZATION=f'Token {self.token.key}')
