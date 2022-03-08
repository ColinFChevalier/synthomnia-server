from django.db import models
from synthomniaapi.models import artist, mood

class Track(models.Model):
    """
    model for Track
    """
    moodId = models.ForeignKey(mood)
    title = models.CharField(
        max_length=50,
        default="Track has not been named"
    )
    bandcampURL = models.CharField(
        max_length=1000,
        null=False,
    )
    artistId = models.ForeignKey(artist)
