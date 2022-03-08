from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    """
    models for Artist
    """
    userId = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )
    bio = models.CharField(
        max_length=500,
        # on_delete=models.CASCADE
    )
