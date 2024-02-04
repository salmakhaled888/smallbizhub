from django.db import models
from Customer_Account.models import CustomerAccount
from Product.models import Product


class Cart_Items(models.Model):
    totalPrice = 0
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="Product in cart")
    user_id = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE, verbose_name="Customer")
    quantity = models.PositiveIntegerField(default=None)
    created_at = models.DateField(default=None)
    modified_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(blank=True,null=True)
    @property
    def total_price(self):
        self.totalPrice += (self.product_id.price)*(self.quantity)
        return self.totalPrice

    def __int__(self):
        return self.id