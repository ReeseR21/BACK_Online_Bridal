from django.http.response import HttpResponse
from django.views import View
from rest_framework import viewsets
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.decorators import api_view, permission_classes
from .models import Onlinebridal
from .serializers import OnlinebridalSerializer
# from django.contrib.auth.models import User


























# class Getstarted(View):

    # onlinebridal = Onlinebridal.objects.get()
    # output = ''
    # for onlinebridal in onlinebridals:
    #     output += f"{onlinebridal.first_name}" + "'s"  " " + "profile in the DB<br>"
    
    # def get(self, request):
    #     return HttpResponse(self.output)

    # onlinebridals = Onlinebridal.objects.all()
    # output = ''
    # for onlinebridal in onlinebridals:
    #     output += f"{onlinebridal.first_name}" + "'s"  " " + "profile in the DB<br>"
    
    # def get(self, request):
    #     return HttpResponse(self.output)

# def onlinebridal(request):
#         return HttpResponse('Bridal profile test function from views')

# Get all bridal info, jwt-token required.

# class OnlinebridalList(APIView):

#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         onlinebridal = Onlinebridal.objects.all()
#         serializer = OnlinebridalSerializer(onlinebridal, many=True)
#         return Response(serializer.data)

# Get all bridal info, no jwt-token required.
# @api_view(['GET'])
# @permission_classes([AllowAny])

# def  get_all_onlinebridal(request):
#     onlinebridal = Onlinebridal.objects.all()
#     serializer = OnlinebridalSerializer(onlinebridal, many=True)
#     return Response(serializer.data)

# # Used for only users that are signed in -- create/add info -- this is a protected endpoint.
# @api_view(['POST', 'GET'])
# @permission_classes([IsAuthenticated])
# def user_onlinebridal(request):

#     print('User', f"{request.user.id} {request.user.email} {request.user.username}")

#     if request.method == 'POST':
#         serializer = OnlinebridalSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Get all bridal data that's tied to a bride/user.
#     elif request.method == 'GET':
#         onlinebridal = Onlinebridal.objects.filter(user_id=request.user.id)
#         serializer = OnlinebridalSerializer(onlinebridal, many=True)
#         return Response(serializer.data)

    