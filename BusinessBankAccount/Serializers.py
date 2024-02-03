from rest_framework import  serializers
from .models import BusinessBankAccount

class BussinessAccountSerializer (serializers.ModelSerializer):

    class Meta:
        model = BusinessBankAccount
        fields = '__all__'