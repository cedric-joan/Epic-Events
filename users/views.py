from .models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from users.serializers import SignupSerializer, EmployeeSerializer


class SignupViewSet(CreateAPIView):

    serializer_class = SignupSerializer

    def get_queryset(self):
        return User.objects.all()


class EmployeeViewSet(ModelViewSet):

    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['role']

    def get_queryset(self):
        return User.objects.all()