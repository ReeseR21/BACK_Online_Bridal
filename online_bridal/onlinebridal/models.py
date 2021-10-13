from django.db import models
from django.contrib.auth.models import User

class Bridalprofile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(blank=False, max_length=25)
    last_name = models.CharField(max_length=25)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zip_code = models.IntegerField(default=True)
    phone = models.CharField(max_length=12)
    email = models.EmailField(blank=False, max_length=50)


class Bridalparty(models.Model):    
    # bridalprofile = models.ForeignKey(Bridalprofile, on_delete=models.CASCADE, default=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    first_name = models.CharField(blank=False, max_length=25)
    last_name = models.CharField(max_length=25)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zip_code = models.IntegerField(default=True)
    phone = models.CharField(max_length=12)
    email = models.EmailField(blank=False, max_length=50)
    participation = models.TextField(max_length=100, default=True)


class Guestlist(models.Model):
    # bridalprofile = models.ForeignKey(Bridalprofile, on_delete=models.CASCADE,default=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    first_name = models.CharField(blank=False, max_length=25)
    last_name = models.CharField(max_length=25)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zip_code = models.IntegerField(default=True)
    phone = models.CharField(max_length=12)
    email = models.EmailField(blank=False, max_length=50)
    family_association = models.TextField(blank=True, max_length=50)


def __str__(self):
    return self.first_name

