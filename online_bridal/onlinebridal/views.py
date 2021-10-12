# from django.http.response import HttpResponse
from rest_framework import viewsets
from .models import Bridalprofile 
from .models import Bridalparty
from .models import Guestlist
from .serializers import BridalprofileSerializer
from .serializers import BridalpartySerializer
from .serializers import GuestlistSerializer

class BridalprofileViewSet(viewsets.ModelViewSet):
    queryset = Bridalprofile.objects.all()
    serializer_class = BridalprofileSerializer

class BridalpartyViewSet(viewsets.ModelViewSet):
    queryset = Bridalparty.objects.all()
    serializer_class = BridalpartySerializer    

class GuestlistViewSet(viewsets.ModelViewSet):
    queryset = Guestlist.objects.all()
    serializer_class = GuestlistSerializer

