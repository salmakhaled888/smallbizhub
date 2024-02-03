from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import BusinessBankAccount
from .Serializers import BussinessAccountSerializer


class BusinessAccountViewSet(viewsets.ModelViewSet):
    serializer_class = BussinessAccountSerializer
    queryset = BusinessBankAccount.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['seller_id']
