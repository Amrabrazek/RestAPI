from rest_framework import serializers
from .models import Cart
from user.serializers import UserSerializer
from product.serializers import ProductSerializer





        
class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = ("id", "quantity", "user", "product")