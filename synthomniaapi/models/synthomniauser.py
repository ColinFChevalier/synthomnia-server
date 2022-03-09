from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from synthomniaapi.models import Mood
User = get_user_model()

class SynthomniaUser(models.Model):
    """
    Synthomnia User class defined
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    bio = models.CharField(
        max_length=150,
        default="I have not created a bio yet"
    )
    profile_image_url = models.URLField(
        null=True,
        max_length=500
    )
    created_on = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    is_artist = models.BooleanField(default=False)
    user_moods = models.ForeignKey(
        Mood,
        null=True,
        on_delete=models.CASCADE
        )
