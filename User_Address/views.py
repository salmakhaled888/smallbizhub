from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .Serializers import UserAddressSerializer
from .models import UserAddress


class UserAddressViewSet(viewsets.ModelViewSet):
    serializer_class = UserAddressSerializer
    queryset = UserAddress.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'user_id']
