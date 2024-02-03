from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import BusinessType
from .Serializers import BusinessTypeSerializer


class BusinessTypeViewSet(viewsets.ModelViewSet):
    serializer_class = BusinessTypeSerializer
    queryset = BusinessType.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['seller_id']
