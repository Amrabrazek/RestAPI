from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password
from user.models import Admin


class Category (models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models. TextField(null=True, blank=True)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)



# User class model
class Product(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    brand = models.CharField(max_length=50, null=False, blank=False)
    instock = models.IntegerField(null=False, blank=False,)
    discountpercentage = models.DecimalField()
    thumbnail = models.ImageField(upload_to='product_images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products') 
    owner = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='products') 
    