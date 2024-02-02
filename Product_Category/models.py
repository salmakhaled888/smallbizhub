from django.db import models

class Product_Categories(models.Model):
    category_name = models.CharField(max_length=100, default=None)
    category_description = models.TextField(max_length=1000, default=None)


    def __str__(self):
        return self.category_name