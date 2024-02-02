from rest_framework import  serializers
from .models import Product_Categories

class ProductCategoriesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Product_Categories
        fields = '__all__'