from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    date_closed = models.DateTimeField()
    # owner = models.CharField(max_length=200)
    sample = models.TextField()
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
    # supporter = models.CharField(max_length=200)
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )

# class Categories(models.Model):
#     category=models.CharField(max_length=200)
#     class Meta:
#         db_table="categories"

        
