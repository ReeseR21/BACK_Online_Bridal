from rest_framework import serializers
from .models import Bridalprofile
from .models import Bridalparty
from .models import Guestlist
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
            
class BridalprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bridalprofile
        fields = ['id', 'first_name', 'last_name', 'street', 'city', 'state', 'zip_code', 'phone', 'email', 'user_id']

class BridalpartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bridalparty
        fields = ['id', 'first_name', 'last_name', 'street', 'city', 'state', 'zip_code', 'phone', 'email', 'participation']

class GuestlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guestlist
        fields = ['id', 'first_name', 'last_name', 'street', 'city', 'state', 'zip_code', 'phone', 'email', 'family_association']