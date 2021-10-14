from rest_framework import serializers
from .models import Vendor, Rating
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
            
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'business_name', 'street', 'city', 'state', 'zip_code', '_business_phone', 'business_email', 'product_service', 'price_range', 'no_of_ratings', 'avg_rating', 'user_id']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'stars', 'user', 'vendor']

