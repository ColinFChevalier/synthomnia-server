from django.db import models
from synthomniaapi.models import track

class Mood(models.Model):
    """
    model for playlists
    """
    name = models.CharField(
        max_length=30,
        on_delete=models.CASCADE
    )
    track = models.ForeignKey(track)
    imgURL = models.CharField(
        max_length=500,
        null=True
    )
