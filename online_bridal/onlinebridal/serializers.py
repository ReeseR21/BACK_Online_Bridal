from rest_framework import serializers
from .models import Bridalprofile
from .models import Bridalparty
from .models import Guestlist

class BridalprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bridalprofile
        fields = ['id', 'first_name', 'last_name', 'street', 'city', 'state', 'zip_code', 'phone', 'email', 'bride', 'groom', 'guest', 'maidofhonor', 'bridesmaid', 'bestman', 'groomsman', 'flower_girl', 'ring_bearer', 'user_id']

class BridalpartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bridalparty
        fields = ['id', 'first_name', 'last_name', 'street', 'city', 'state', 'zip_code', 'phone', 'email''user_id']

class GuestlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guestlist
        fields = ['id', 'first_name', 'last_name', 'street', 'city', 'state', 'zip_code', 'phone', 'email''user_id']