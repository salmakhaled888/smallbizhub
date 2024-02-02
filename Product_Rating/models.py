from django.db import models
from Product.models import Product
from Customer_Account.models import CustomerAccount
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Product_Rating(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="Product ID")
    user_id = models.ForeignKey(CustomerAccount,on_delete=models.CASCADE,verbose_name="Customer ID")
    rating = models.PositiveIntegerField(default=None,
                                         validators=[
                                             MaxValueValidator(5),
                                             MinValueValidator(0)
                                         ]
                                         )
    created_at = models.DateTimeField(default=None)

    def __str__(self):
        return self.product_id.product_name
