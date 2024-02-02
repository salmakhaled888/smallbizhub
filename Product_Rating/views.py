from rest_framework import viewsets, filters
from .models import Product_Rating
from .Serializers import ProductRatingSerializer


class ProductRatingViewSet(viewsets.ModelViewSet):
    serializer_class = ProductRatingSerializer
    queryset = Product_Rating.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id','rating','user_id__id')
