from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .Serializers import SellerAccountSerializer
from .models import SellerAccount


class SellerAccountViewSet(viewsets.ModelViewSet):
    serializer_class = SellerAccountSerializer
    queryset = SellerAccount.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','user_id','first_name', 'last_name', 'business_name', 'business_field']

