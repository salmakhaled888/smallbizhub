from django.db import models
from Customer_Account.models import CustomerAccount

class Order_Details(models.Model):
    user_id = models.ForeignKey(CustomerAccount,on_delete= models.CASCADE,verbose_name='Customer ID')
    total = models.DecimalField(max_digits=100000, decimal_places=3, default=None)
    status = models.CharField(max_length=1000, default=None)
    created_at = models.DateField()
    modified_at = models.DateField()
    deleted_at = models.DateField(blank=True,null=True)
    def __int__(self):
        return self.id
