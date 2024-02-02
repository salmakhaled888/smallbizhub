from rest_framework import  serializers
from .models import SellerShop

class SellerShopSerializer (serializers.ModelSerializer):
    class Meta:
        model = SellerShop
        fields = '__all__'