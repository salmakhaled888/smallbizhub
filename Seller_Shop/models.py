from django.db import models
from Seller_Account.models import SellerAccount


class SellerShop (models.Model):
    seller_id = models.OneToOneField(SellerAccount,default= None,on_delete=models.CASCADE,verbose_name="Seller ID")
    shop_name = models.CharField(max_length = 100, default=None)
    facebook_link = models.CharField(max_length=100, default=None)
    instagram_link = models.CharField(max_length=100, default=None)
    website_link = models.CharField(max_length=100, default=None)
    location = models.CharField(max_length=100, default=None)
    def __str__(self):
        return self.shop_name

