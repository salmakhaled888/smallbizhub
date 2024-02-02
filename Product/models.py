from django.db import models
from Product_Category.models import Product_Categories
from Seller_Account.models import SellerAccount


class Product(models.Model):
    product_name = models.CharField(max_length=100, default=None)
    product_image = models.ImageField(upload_to='Product Images')
    product_description = models.TextField(max_length=1000, default=None)
    SKU = models.CharField(max_length=12, default=None)
    category_id = models.ForeignKey(Product_Categories,on_delete=models.CASCADE,verbose_name="Category ID")
    seller_id = models.ForeignKey(SellerAccount, on_delete=models.CASCADE, verbose_name="Seller ID")
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10000000,decimal_places=3,default=None)
    created_at = models.DateField(default=None)
    modified_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.product_name
