from django.db import models
# from synthomniaapi.models import Track

class Mood(models.Model):
    """
    model for playlists
    """
    name = models.CharField(max_length=30)
    imgURL = models.CharField(
        max_length=500,
        null=True
    )
