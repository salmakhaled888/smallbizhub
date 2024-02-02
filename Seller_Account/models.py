from django.db import models

from User.models import CustomUser


class SellerAccount (models.Model):
    national_id = models.CharField(null= True,blank=True,max_length=14,default=None)
    user_name = models.CharField(max_length=100, default=None, unique=True,null=True,blank=True)
    user_id = models.OneToOneField(CustomUser,default= None,on_delete=models.CASCADE,verbose_name="User ID")
    first_name = models.CharField(max_length = 100, default=None)
    last_name = models.CharField(max_length=100, default=None)
    telephone = models.PositiveIntegerField(default=None)
    created_at = models.DateField(default=None)
    modified_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.first_name

