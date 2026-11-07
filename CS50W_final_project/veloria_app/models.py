from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    vocabulary_ids = models.JSONField(default=list)


class Story(models.Model):
    title = models.CharField(max_length=200)
    level = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.title} ({self.level})"

class Content(models.Model):
    story_id = models.ForeignKey(Story, on_delete=models.CASCADE)
    sentence = models.TextField()
    translation = models.TextField()
