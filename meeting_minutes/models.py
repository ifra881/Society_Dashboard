from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class meeting(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField(default=False)
    time = models.TimeField(default=False)
    location = models.TextField(max_length=200)
    agenda = models.TextField(max_length=1000)
    members = models.TextField(max_length=200)
    decision = models.TextField(max_length=1000)

    
class schedule(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField(default=False)
    time = models.TimeField(default=False)
    location = models.TextField(max_length=200)



