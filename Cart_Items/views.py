from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Cart_Items
from .Serializers import CartItemSerializer


class CartItemsViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    queryset = Cart_Items.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['users_id','product_id']
