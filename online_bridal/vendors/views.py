from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Vendor
from .serializers import VendorSerializer
from django.contrib.auth.models import User

# Create your views here.
# Get all bridal info, jwt-token required.

class VendorList(APIView):
# Change AllowAny to IsAuthenticated to require a jwt token
    permission_classes = [AllowAny]

    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

# Get all bridal info, no jwt-token required.
# @api_view(['GET'])
# @permission_classes([AllowAny])

# def  get_all_vendors(request):
#     vendors = Vendors.objects.all()
#     serializer = VendorsSerializer(vendors, many=True)
#     return Response(serializer.data)

# Used for only users that are signed in -- create/add info -- this is a protected endpoint.
# @api_view(['POST', 'GET'])
# @permission_classes([AllowAny])
# def user_vendors(request):

    # print('User', f"{request.user.id} {request.user.email} {request.user.username}")

    # if request.method == 'POST':
    #     serializer = VendorsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(user=request.user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get all bridal data that's tied to a bride/user.
    # elif request.method == 'GET':
    #     vendors = Vendors.objects.filter(user_id=request.user.id)
    #     serializer = VendorsSerializer(vendors, many=True)
    #     return Response(serializer.data)