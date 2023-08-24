from .models import User
from rest_framework.generics import CreateAPIView
from users.serializers import UserSerializer

class UserViewSet(CreateAPIView):

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)