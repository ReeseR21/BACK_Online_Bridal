from rest_framework import serializers
from .models import Onlinebridal

class OnlinebridalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onlinebridal
        fields = ['id', 'first_name', 'last_name', 'street', 'city', 'state', 'zip_code', 'phone', 'bride', 'groom', 'guest', 'maidofhonor', 'bridesmaid', 'bestman', 'groomsman', 'flower_girl', 'ring_bearer', 'user_id']

    