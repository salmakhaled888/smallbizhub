from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .Serializers import CustomerAccountSerializer
from .models import CustomerAccount


class CustomerAccountViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerAccountSerializer
    queryset = CustomerAccount.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','user_id','first_name','last_name']
