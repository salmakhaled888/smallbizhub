from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets,filters
from .models import Product_Categories
from .Serializers import ProductCategoriesSerializer

class ProductCategoryViewSet(viewsets.ModelViewSet):

    serializer_class = ProductCategoriesSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = 'category_name'
    queryset = Product_Categories.objects.all()


