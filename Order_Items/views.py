from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import Order_Items
from .Serializers import OrderItemSerializer

class OrderItemsViewSet(viewsets.ModelViewSet):

    serializer_class = OrderItemSerializer
    queryset = Order_Items.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'order_id', 'product_id']
