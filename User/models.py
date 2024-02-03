from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class MyUserManager(BaseUserManager):

    def create_user(self, email, password=None ):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,password=None):

        user = self.create_user(
            email,
            password=password
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(max_length=255,unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()


    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email



