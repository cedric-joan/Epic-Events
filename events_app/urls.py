from django.urls import path, include
from rest_framework import routers
from .views import ClientView, ContractView, EventView

router = routers.SimpleRouter()
router.register('clients', ClientView, basename='clients')
router.register('contracts', ContractView, basename='contracts')
router.register('events', EventView, basename='events')

urlpatterns = [
    path('', include(router.urls))
]