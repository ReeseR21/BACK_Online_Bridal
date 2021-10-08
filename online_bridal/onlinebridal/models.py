from django.db import models
from django.contrib.auth.models import User

class Onlinebridal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    street = models.CharField(max_length=75)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zip_code = models.IntegerField(default=True)
    phone = models.CharField(max_length=12)
    email = models.CharField(default=True, max_length=200)
    bride = models.BooleanField(null=True)
    groom = models.BooleanField(null=True)
    guest = models.BooleanField(null=True)
    maidofhonor = models.BooleanField(null=True)
    bridesmaid = models.BooleanField(null=True)
    bestman = models.BooleanField(null=True)
    groomsman = models.BooleanField(null=True)
    flower_girl = models.BooleanField(null=True)
    ring_bearer = models.BooleanField(null=True)

   

