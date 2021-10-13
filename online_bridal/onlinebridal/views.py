# from django.http.response import HttpResponse
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from .models import Bridalprofile, Bridalparty, Guestlist 
from .serializers import BridalprofileSerializer, BridalpartySerializer, GuestlistSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BridalprofileViewSet(viewsets.ModelViewSet):
    queryset = Bridalprofile.objects.all()
    serializer_class = BridalprofileSerializer
    authentication_classes = (TokenAuthentication,)

class BridalpartyViewSet(viewsets.ModelViewSet):
    queryset = Bridalparty.objects.all()
    serializer_class = BridalpartySerializer    
    authentication_classes = (TokenAuthentication,)

class GuestlistViewSet(viewsets.ModelViewSet):
    queryset = Guestlist.objects.all()
    serializer_class = GuestlistSerializer
    authentication_classes = (TokenAuthentication,)

