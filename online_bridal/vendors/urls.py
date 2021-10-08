from django.urls import path
from vendors import views

# url pattern when jwt-token required.

urlpatterns = [
    path('', views.VendorList.as_view())
   ]

# Url pattern used with get all bridal info when no token required.

# urlpatterns = [
#     path('all/', views.get_all_vendors),
#     path('', views.user_vendors)
#    ]
