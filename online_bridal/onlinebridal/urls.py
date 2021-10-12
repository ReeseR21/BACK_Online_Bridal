from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls import include
from .views import BridalprofileViewSet

router = routers.DefaultRouter()
router.register('bridalprofile', BridalprofileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('new/', admin.site.urls), 
    
]

