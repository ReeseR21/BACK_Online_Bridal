from rest_framework import serializers
from .models import GuestList, Onlinebridal
from .models import BridalParty
from .models import GuestList

class OnlinebridalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onlinebridal
        fields = ['id', 'first_name', 'last_name', 'street', 'city', 'state', 'zip_code', 'phone', 'email', 'bride', 'groom', 'guest', 'maidofhonor', 'bridesmaid', 'bestman', 'groomsman', 'flower_girl', 'ring_bearer', 'user_id']

class BridalPartySerializer(serializers.ModelSerializer):
    class Meta:
        model = BridalParty
        fields = ['id', 'first_name', 'last_name', 'street', 'city', 'state', 'zip_code', 'phone', 'email''user_id']

class GuestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestList
        fields = ['id', 'first_name', 'last_name', 'street', 'city', 'state', 'zip_code', 'phone', 'email''user_id']