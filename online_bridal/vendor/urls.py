from rest_framework import routers
from django.conf.urls import  include
from django.urls import path, include
from .views import VendorViewSet, RatingViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('vendor', VendorViewSet)
router.register('ratings', RatingViewSet)


urlpatterns = [
    path('', include(router.urls)),
  
]
