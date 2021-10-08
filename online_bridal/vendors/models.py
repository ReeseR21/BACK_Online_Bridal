from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    business_name = models.CharField(max_length=75)
    street = models.CharField(max_length=75)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zip_code = models.IntegerField(default=True)
    business_phone = models.CharField(max_length=12)
    business_email = models.CharField(default=True,max_length=200)
    service = models.CharField(max_length=75)
    
# def __str__(self):
#     return self.first_name