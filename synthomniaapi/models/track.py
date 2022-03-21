from django.db import models
from synthomniaapi.models import Artist, Mood

class Track(models.Model):
    """
    model for Track
    """
    title = models.CharField(
        max_length=50,
        default="Track has not been named"
    )
    bandcampURL = models.CharField(
        max_length=1000,
        null=False,
    )
    mood = models.ForeignKey(
        Mood,
        on_delete=models.CASCADE
        )
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE
        )
