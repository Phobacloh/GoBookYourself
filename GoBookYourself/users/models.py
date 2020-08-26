from django.contrib.auth.models import AbstractUser
from django.db import models
from django.http import Http404
from rest_framework.response import Response

# Create your models here.

class CustomUser(AbstractUser):
    tagline = models.CharField(max_length=200)
    bio = models.TextField()
    profile_pic = models.URLField()
    CATEGORY_CHOICES = (
        ('Anything', 'NA'),
        ('Young Adult', 'YA'),
        ('Romance', 'RO'),
        ('Fantasy', 'FA'),
        ('Sci-Fi', 'SF'),
        ('Non-Fiction', 'NF'),
        ('Graphic Novels & Comics', 'GN'),
        ('Mystery', 'MY'),
        ('Historical Fiction', 'HF'),
        ('Horror', 'HO'),
        ('Thriller', 'TH'),
        ('Poetry', 'PO')
    )
    favorite_genre = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.username