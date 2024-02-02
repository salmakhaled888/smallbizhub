from django.db import models
from User.models import CustomUser
class UserAddress (models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,verbose_name="User ID")
    address_line1 = models.CharField(max_length= 40, default=None)
    address_line2 = models.CharField(max_length= 40, default=None)
    city = models.CharField(max_length= 40, default=None)
    postal_code = models.CharField(max_length= 40, default=None)
    country = models.CharField(max_length= 40, default=None)
    def __str__(self):
        return self.user_id.email