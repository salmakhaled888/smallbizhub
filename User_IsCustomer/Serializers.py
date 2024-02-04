from rest_framework import  serializers
from .models import UserIsCustomer

class UserIsCustomerSerializer (serializers.ModelSerializer):

    class Meta:
        model = UserIsCustomer
        fields = '__all__'