from django.urls import path
# from .views import OnlinebridalList
from onlinebridal import views


urlpatterns = [
    path('', views.OnlinebridalList.as_view())
   ]