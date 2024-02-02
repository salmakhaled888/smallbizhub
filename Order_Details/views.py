from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Order_Details
from .Serializers import OrderDetailSerializer

class OrderDetailsViewSet(viewsets.ModelViewSet):

    serializer_class = OrderDetailSerializer
    queryset = Order_Details.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'user_id']
