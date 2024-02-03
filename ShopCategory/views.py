from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import ShopCategory
from .Serializers import ShopCategorySerializer


class ShopCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ShopCategorySerializer
    queryset = ShopCategory.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['seller_id','shop_id']
