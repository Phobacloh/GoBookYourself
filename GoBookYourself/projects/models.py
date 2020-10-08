from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now=True)
    date_closed = models.DateTimeField()
    # owner = models.CharField(max_length=200)
    sample = models.TextField()
    CATEGORY_CHOICES = (
        ('Anything', 'Anything'),
        ('Young-Adult', 'Young-Adult'),
        ('Romance', 'Romance'),
        ('Fantasy', 'Fantasy'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Graphic-Novels-and-Comics', 'Graphic-Novels-and-Comics'),
        ('Mystery', 'Mystery'),
        ('Historical-Fiction', 'Historical-Fiction'),
        ('Horror', 'Horror'),
        ('Thriller', 'Thriller'),
        ('Poetry', 'Poetry')
    )
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )

       # supporter = models.CharField(max_length=200)     
