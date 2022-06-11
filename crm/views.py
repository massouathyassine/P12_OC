from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
import logging

from .serializers import ClientSerializer, ContractSerializer, EventSerializer
from .models import Client, Contract, Event
from .permissions import ClientPermission, ContractPermission, EventPermission
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
logger = logging.getLogger('django')


class ClientViewSet(ModelViewSet):
    """
    API endpoints to create, view, edit or delete a client
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated, ClientPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name']


class ContractViewSet(ModelViewSet):
    """
    API endpoints to create, view, edit or delete a contract
    """
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated, ContractPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sales_contact']


class EventViewSet(ModelViewSet):
    """
    API endpoints to create, view, edit or delete an event
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, EventPermission]
