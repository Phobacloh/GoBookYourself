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
        ('YA', 'Young Adult'),
        ('RO', 'Romance'),
        ('FA', 'Fantasy'),
        ('SF', 'Sci-Fi'),
        ('NF', 'Non-Fiction'),
        ('GN', 'Graphic Novels & Comics'),
        ('MY', 'Mystery'),
        ('HF', 'Historical Fiction'),
        ('HO', 'Horror'),
        ('TH', 'Thriller'),
        ('PO', 'Poetry')
    )
    favorite_genre = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.username