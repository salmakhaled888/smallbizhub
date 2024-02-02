from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .Serializers import SellerShopSerializer
from .models import SellerShop


class SellerShopViewSet(viewsets.ModelViewSet):
    serializer_class = SellerShopSerializer
    queryset = SellerShop.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

