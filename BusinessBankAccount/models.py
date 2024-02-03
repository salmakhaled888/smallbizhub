from django.db import models
from Customer_Account.models import CustomerAccount
from Seller_Account.models import SellerAccount

class BusinessBankAccount(models.Model):
    seller_id = models.OneToOneField(SellerAccount, on_delete=models.CASCADE, verbose_name="Seller")
    bank_name = models.CharField(default=None, max_length=100)
    account_number = models.PositiveIntegerField(default=None)
    bsb_code = models.CharField(default=None,max_length=100)
    def __int__(self):
        return self.id