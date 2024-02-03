from django.db import models
from User.models import CustomUser
# Create your models here.
class CustomerAccount(models.Model):
    user_id = models.OneToOneField(CustomUser,default= None,on_delete=models.CASCADE,verbose_name="User ID")
    user_name = models.CharField(max_length=100, default=None,blank=True,null=True,unique=True)
    first_name = models.CharField(max_length=100, default=None)
    last_name = models.CharField(max_length=100, default=None)
    telephone = models.PositiveIntegerField(default=None)
    address_line1 = models.CharField(max_length=40, default=None,null=True,blank=True)
    address_line2 = models.CharField(max_length=40, default=None,null=True,blank=True)
    city = models.CharField(max_length=40, default=None,null=True,blank=True)
    postal_code = models.CharField(max_length=40, default=None,null=True,blank=True)
    country = models.CharField(max_length=40, default=None,null=True,blank=True)
    created_at = models.DateField(default=None)
    modified_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.first_name
