from django.db import models
# from synthomniaapi.models import Track

class Mood(models.Model):
    """
    model for playlists
    """
    name = models.CharField(
        max_length=30,
        # on_delete=models.CASCADE
    )
    # track = models.ForeignKey(
    #     Track,
    #     related_name="mood_track",
    #     on_delete=models.CASCADE
    #     )
    imgURL = models.CharField(
        max_length=500,
        null=True
    )
