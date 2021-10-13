from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls import include
from .views import BridalprofileViewSet, BridalpartyViewSet, GuestlistViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('bridalprofile', BridalprofileViewSet)
router.register('bridalparty', BridalpartyViewSet)
router.register('guestlist', GuestlistViewSet)

urlpatterns = [
    path('', include(router.urls)),
  
]

