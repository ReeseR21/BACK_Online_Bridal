from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Vendor, Rating
from .serializers import Vendor, Rating
from .serializers import VendorSerializer, RatingSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset =Vendor.objects.all()
    serializer_class = VendorSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    
    @action(detail=True, methods=['POST'])
    def rate_vendor(self, request, pk=None):
        if 'stars' in request.data:

            vendor = Vendor.objects.get(id=pk)
            stars = request.data['stars']
            # user = request.user
            user = User.objects.get(id=1)

            try:
                rating = Rating.objects.get(user=user.id, vendor=vendor.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating updated', 'result': serializer.data}
                return Response(Response, status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user=user, vendor=vendor, stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating created', 'result': serializer.data}
                return Response(Response, status=status.HTTP_200_OK)
            
        else:
            response = {'message': 'You need to provide a star value'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer    
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated, )

# class GuestlistViewSet(viewsets.ModelViewSet):
#     queryset = Guestlist.objects.all()
#     serializer_class = GuestlistSerializer
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated, )