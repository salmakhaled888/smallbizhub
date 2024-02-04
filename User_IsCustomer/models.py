from django.db import models
from User.models import CustomUser


class UserIsCustomer(models.Model):
    user_id = models.OneToOneField(CustomUser,on_delete=models.CASCADE,verbose_name="User")
    is_customer = models.BooleanField(default=None)

    def __int__(self):
        return self.id