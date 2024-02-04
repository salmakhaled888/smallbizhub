from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import UserIsCustomer
from .Serializers import UserIsCustomerSerializer


class UserIsCustomerViewSet(viewsets.ModelViewSet):
    serializer_class = UserIsCustomerSerializer
    queryset = UserIsCustomer.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id','is_customer']
