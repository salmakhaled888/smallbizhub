from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import Product
from .Serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    filter_backends =(filters.SearchFilter,DjangoFilterBackend)
    search_fields = ('product_name', 'product_image', 'product_description', 'category_id__category_name')
    queryset = Product.objects.all()
