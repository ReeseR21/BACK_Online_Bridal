from django.db import models
from django.contrib.auth.models import User

class Vendorprofile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business_name = models.CharField(blank=False, max_length=25)
    first_name = models.CharField(blank=False, max_length=25)
    last_name = models.CharField(max_length=25)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zip_code = models.IntegerField(default=True)
    business_phone = models.CharField(max_length=12)
    business_email = models.EmailField(blank=False, max_length=50)
    product_service = models.TextField(max_length=100)

def __str__(self):
    return self.product_service