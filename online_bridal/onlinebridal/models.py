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
    phone = models.IntegerField(default=True)
    bride = models.BooleanField(null=True)
    groom = models.BooleanField(null=True)
    guest = models.BooleanField(null=True)
    maidofhonor = models.BooleanField(null=True)
    bridesmaid = models.BooleanField(null=True)
    bestman = models.BooleanField(null=True)
    groomsman = models.BooleanField(null=True)

    def __str__(self):
        return self.name

# Create your models here.
