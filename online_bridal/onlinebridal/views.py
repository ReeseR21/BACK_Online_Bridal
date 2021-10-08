# Create your views here.
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Onlinebridal


# Create your views here.
def index(request):
    all_brides = Onlinebridal.objects.all()
    context = {
        'all_brides': all_brides
    }
    return render(request, 'Onlinebridals/index.html', context)

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