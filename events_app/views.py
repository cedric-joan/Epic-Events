from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .models import Client, Contract, Event
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ClientSerializer, ContractSerializer, EventSerializer

class ClientView(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['fisrt_name', 'last_name', 'company_name']


    def get_queryset(self):
        # if self.request.user.role == "SUP":
        #     return Client.objects.filter(sales_contact=self.request.user)
        # elif self.request.user.role == "SAL":
        #     return Client.objects.filter(support_contact=self.request.user)
        # else:
            return Client.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

class ContractView(ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['contract_status', 'remaining_amount', 'date_created']

    def get_queryset(self):
        # if self.request.user.role == "SUP":
        #     return Contract.objects.filter(sales_contact=self.request.user)
        # elif self.request.user.role == "SAL":
        #     return Contract.objects.filter(support_contact=self.request.user)
        # else:
            return Contract.objects.all()

    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

class EventView(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['fisrt_name', 'last_name', 'company_name']

    def get_queryset(self):
        if self.request.user.role == "SUP":
            return Event.objects.filter(sales_contact=self.request.user)
        elif self.request.user.role == "SAL":
            return Event.objects.filter(support_contact=self.request.user)
        else:
            return Event.objects.all()
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)