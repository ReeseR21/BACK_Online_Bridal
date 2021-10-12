# from django.http.response import HttpResponse
# from django.views import View

# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.decorators import api_view, permission_classes
# from .models import Vendor
# from .serializers import VendorSerializer
# from django.contrib.auth.models import User


# class Listservice(View):
    
#     vendors = Vendor.objects.filter(is_formalwear=True)
#     output = ''
#     for vendor in vendors:
#         output += f"{Vendor.first_name}" + "'s"  " " + "profile with ID {vendor.id}<br>"
    
#     def get(self, request):
#         return HttpResponse(self.output)

#     vendor = Vendor.objects.all()
#     output = ''
#     for vendor in vendors:
#         output += f"{vendor.first_name}" + "'s"  " " + "profile in the DB<br>"
    
#     def get(self, request):
#         return HttpResponse(self.output)

# def vendor(request):
#     return HttpResponse('Bridal profile test function from views')



# Create your views here.
# Get all bridal info, jwt-token required. This is a class view that can not be used with a function view that allows a signed-in user to POST. Like that in superheroes and trash collector.

# class VendorList(APIView):
# Change AllowAny to IsAuthenticated to require a jwt token
    # permission_classes = [AllowAny]

    # def get(self, request):
    #     vendor = Vendor.objects.all()
    #     serializer = vendorerializer(vendor, many=True)
    #     return Response(serializer.data)

# Get all bridal info, no jwt-token required.
# These are metadata or attributes
# @api_view(['GET'])
# @permission_classes([AllowAny])

# def  get_all_vendors(request):
#     vendors = Vendor.objects.all()
#     serializer = VendorSerializer(vendors, many=True)
#     return Response(serializer.data)

# # Used for only users that are signed in -- create/add info -- this is a protected endpoint.
# @api_view(['POST', 'GET', 'PUT'])
# @permission_classes([IsAuthenticated])
# def user_vendors(selF, request, pk):

#     print('User', f"{request.user.id} {request.user.email} {request.user.username}")

#     if request.method == 'POST':
#         # request.user
#         serializer = VendorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Get all bridal data that's tied to a bride/user.
#     elif request.method == 'GET':
#         vendors = Vendor.objects.filter()
#         serializer = VendorSerializer(vendors, many=True)
#         return Response(serializer.data)

    # elif request.method == 'PUT':
    #     vendors = Vendor.object(self, request, pk)
    #     serializer = VendorSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

        # user_id=request.user.id
        # user=request.user