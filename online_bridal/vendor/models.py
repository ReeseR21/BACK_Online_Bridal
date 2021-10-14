from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Vendor(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    business_name = models.CharField(blank=False, max_length=25)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zip_code = models.IntegerField(default=True)
    business_phone = models.CharField(max_length=12)
    business_email = models.EmailField(blank=False, max_length=50)
    product_service = models.TextField(max_length=100)
    price_range = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images/', blank=True)


    def no_of_ratings(self):
        ratings = Rating.objects.filter(vendor=self)
        return len(ratings)

    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(vendor=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

class Rating(models.Model):    
    # bridalprofile = models.ForeignKey(Bridalprofile, on_delete=models.CASCADE, default=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'vendor'),)
        index_together = (('user', 'vendor'),)

def __str__(self):
    return self.product_service