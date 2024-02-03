from django.db import models
from Seller_Account.models import SellerAccount
from Seller_Shop.models import SellerShop


class BusinessType(models.Model):
    seller_id = models.OneToOneField(SellerAccount,on_delete=models.CASCADE,verbose_name="Seller")
    business_type = models.CharField(default=None,max_length=100)

    def __int__(self):
        return self.id