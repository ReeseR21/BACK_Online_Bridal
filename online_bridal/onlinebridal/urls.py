from django.urls import path
# from onlinebridal import views
from . import views
# from .views import Getstarted
# from .views import Vendors
from rest_framework import routers

# url pattern when jwt-token required.

# urlpatterns = [
#     path('', views.OnlinebridalList.as_view())
#    ]

# Url pattern used with get all bridal info when no token required.

urlpatterns = [
    # path('all/', views.get_all_onlinebridal),
    path('', views.onlinebridal),
    # path('getstarted/', Getstarted.as_view()),
    # path('vendors/', Vendors.as_view())

   ]

