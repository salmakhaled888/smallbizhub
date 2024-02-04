from django.db import models
from Product.models import Product
from Order_Details.models import Order_Details


class Order_Items(models.Model):
    order_id = models.ForeignKey(Order_Details,on_delete=models.CASCADE,verbose_name="Order ID")
    product_id = models.ForeignKey(Product,on_delete= models.CASCADE,verbose_name="Products",null=True)
    quantity = models.PositiveIntegerField(default=None)
    created_at = models.DateField()
    modified_at = models.DateField()
    deleted_at = models.DateField(null=True, blank=True)
    def __int__(self):
        return self.order_id
