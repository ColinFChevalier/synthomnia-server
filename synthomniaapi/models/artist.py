from django.db import models
from django.contrib.auth import get_user_model
from synthomniaapi.models.mood import Mood
User = get_user_model()

class Artist(models.Model):
    """
    models for Artist
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )
    bio = models.CharField(
        max_length=500,
        # on_delete=models.CASCADE
    )
    mood = models.ManyToManyField(
        Mood,
        related_name="mood"
    )
