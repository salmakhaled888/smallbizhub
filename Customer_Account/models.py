from django.db import models
from User.models import CustomUser
# Create your models here.
class CustomerAccount(models.Model):
    user_id = models.OneToOneField(CustomUser,default= None,on_delete=models.CASCADE,verbose_name="User ID")
    user_name = models.CharField(max_length=100, default=None,blank=True,null=True,unique=True)
    first_name = models.CharField(max_length=100, default=None)
    last_name = models.CharField(max_length=100, default=None)
    telephone = models.PositiveIntegerField(default=None)
    created_at = models.DateField(default=None)
    modified_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.first_name