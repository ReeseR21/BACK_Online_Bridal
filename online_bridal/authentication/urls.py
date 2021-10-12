from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls import include


# from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from .views import RegisterView

router = routers.DefaultRouter()

urlpatterns = [
        path('', include(router.urls)), 

]


# path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('register/', RegisterView.as_view(), name='register')