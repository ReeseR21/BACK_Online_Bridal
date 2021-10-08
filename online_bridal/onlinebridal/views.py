from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Onlinebridal
from .serializers import OnlinebridalSerializer
from django.contrib.auth.models import User

class OnlinebridalList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        onlinebridal = Onlinebridal.objects.all()
        serializer = OnlinebridalSerializer(onlinebridal, many=True)
        return Response(serializer.data)

# def detail(request, bride_id):
#     single_bride = Onlinebridal.objects.get(pk=bride_id)
#     context = {
#         'single_bride': single_bride
#     }
#     return render(request, 'Onlinebridals/detail.html', context)

# def create(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         alter_ego = request.POST.get('alter_ego')
#         primary = request.POST.get('primary')
#         secondary = request.POST.get('secondary')
#         catchphrase = request.POST.get('catchphrase')
#         new_hero = Onlinebridal(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary, catch_phrase=catchphrase)
#         new_hero.save()
#         return HttpResponseRedirect(reverse('Onlinebridals:index'))
#     else:
#         return render(request, 'Onlinebridals/create.html')

# def edit(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         alter_ego = request.POST.get('alter_ego')
#         primary = request.POST.get('primary')
#         secondary = request.POST.get('secondary')
#         catchphrase = request.POST.get('catchphrase')
#         current_hero = Onlinebridal(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary, catch_phrase=catchphrase)
#         current_hero.save()
#         return HttpResponseRedirect(reverse('Onlinebridals:index'))
#     else:
#         return render(request, 'Onlinebridals/create.html')