from rest_framework import  serializers
from .models import Product_Rating

class ProductRatingSerializer (serializers.ModelSerializer):
    class Meta:
        model = Product_Rating
        fields = '__all__'