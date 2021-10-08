from django.urls import path
from onlinebridal import views

# url pattern when jwt-token required.

# urlpatterns = [
#     path('', views.OnlinebridalList.as_view())
#    ]

# Url pattern used with get all bridal info when no token required.

urlpatterns = [
    path('all/', views.get_all_onlinebridal),
    path('', views.user_onlinebridal)
   ]