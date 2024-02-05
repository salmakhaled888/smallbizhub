from rest_framework import  serializers
from .models import Cart_Items

class CartItemSerializer (serializers.ModelSerializer):

    class Meta:
        model = Cart_Items
        fields = ['id','product_id','users_id','quantity','created_at','modified_at','deleted_at','total_price']