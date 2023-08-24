from django.urls import path
from users.views import UserViewSet
# from rest_framework_simplejwt.views 


urlpatterns = [
    path('home/', UserViewSet.as_view(), name="home")
]
