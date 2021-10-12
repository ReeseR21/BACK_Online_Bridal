# from django.db import models
# from django.contrib.auth.models import User

# class Vendor(models.Model):
#     # user = models.ForeignKey(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=25)
#     last_name = models.CharField(max_length=25)
#     business_name = models.CharField(max_length=75)
#     street = models.CharField(max_length=75)
#     city = models.CharField(max_length=25)
#     state = models.CharField(max_length=25)
#     zip_code = models.IntegerField(default=True)
#     business_phone = models.CharField(max_length=12)
#     business_email = models.EmailField(default=True, max_length=75)
#     # service = models.CharField(blank=False, max_length=75)
#     is_formalwear = models.BooleanField(default=False)
#     is_music = models.BooleanField(default=False)
#     is_venue = models.BooleanField(default=False)
#     is_bakery = models.BooleanField(default=False)
#     is_weddingconsultant = models.BooleanField(default=False)
#     is_formaldance = models.BooleanField(default=False)
#     is_florist = models.BooleanField(default=False)
#     is_photography = models.BooleanField(default=False)
#     is_jeweler = models.BooleanField(default=False)
#     price_range = models.DecimalField(default=0, max_digits=6, decimal_places=2)
#     description = models.TextField(max_length=250, blank=True)
#     photo = models.ImageField(upload_to='photos/', blank=True)
    
# def __str__(self):
#     return self.first_name