from django.db import models
from synthomniaapi.models import artist, mood

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
    moodId = models.ForeignKey(
        mood,
        on_delete=models.CASCADE
        )
    artistId = models.ForeignKey(
        artist,
        on_delete=models.CASCADE
        )
