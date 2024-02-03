from django.db import models
from Customer_Account.models import CustomerAccount
from Seller_Account.models import SellerAccount
from Seller_Shop.models import SellerShop


class ShopCategory(models.Model):
    seller_id = models.OneToOneField(SellerAccount,on_delete=models.CASCADE,verbose_name="Seller")
    shop_id = models.OneToOneField(SellerShop, on_delete=models.CASCADE, verbose_name="Shop")
    category_name = models.CharField(default=None,max_length=100)

    def __int__(self):
        return self.id