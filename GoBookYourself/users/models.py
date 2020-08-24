from django.contrib.auth.models import AbstractUser
from django.db import models
from django.http import Http404
from rest_framework.response import Response

# Create your models here.

class CustomUser(AbstractUser):
    tagline = models.CharField(max_length=200)
    bio = models.TextField()
    profile_pic = models.URLField()
    def __str__(self):
        return self.username