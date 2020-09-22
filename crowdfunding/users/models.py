from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models


class CustomUser(AbstractUser):
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    country = models.CharField(max_length=200, blank=True)
    profile_image = models.CharField(max_length=200, blank=True)
    user_bio = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.username


