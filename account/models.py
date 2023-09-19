from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import BigAutoField
from datetime import datetime, date
from django.db.models.signals import post_save
from django.dispatch import receiver  


# Create your models here.


class User(AbstractUser):
    # id= models.AutoField(primary_key=True, default=True)
    name= models.CharField(max_length=250,null=False,blank=True)
    updated_on = models.DateTimeField(default=datetime.now, blank=True)
    is_excom= models.BooleanField('Is Excom', default=False)
    is_director = models.BooleanField('Is Director', default=False)
    is_member = models.BooleanField('Is Member', default=False)

class Members(models.Model):
    # id= models.AutoField(primary_key=True, default=True)
    name = models.CharField(max_length=250,null=True,blank=True)
    domain = models.CharField(max_length=250,null=True,blank=True)
    department = models.CharField(max_length=250,null=True,blank=True)
    year = models.CharField(max_length=250,null=True,blank=True)
    contact_number = models.CharField(max_length=250,null=True,blank=True)
    email = models.EmailField(max_length=250,null=False,blank=True)
    updated_on = models.DateTimeField(User, default=datetime.now, blank=True)

class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.CharField(max_length=250,null=True,blank=True)
    taskcom = models.BooleanField('complete' , default=False)
    task = models.CharField(max_length=1000,null=True,blank=True)
    completion_date = models.DateField(null=True, blank=True)


