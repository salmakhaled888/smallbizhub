from rest_framework import  serializers
from .models import Order_Details

class OrderDetailSerializer (serializers.ModelSerializer):
    class Meta:
        model = Order_Details
        fields = '__all__'