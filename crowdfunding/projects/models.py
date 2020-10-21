from django.contrib.auth import get_user_model
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        #.PROTECT to prevent projects that have pledges from being deleted
        related_name='owner_projects'
    )



class Pledge(models.Model):
    image = models.URLField(default="https://via.placeholder.com/300.jpg")
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project', 
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
        related_name = 'supporter_pledges'
    )






