from django.db import models
from user.models import User
from product.models import Product
# Create your models here.
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} ({self.quantity}) in Cart for {self.user.username}"

    def get_total_price(self):
        return self.quantity * self.product.price