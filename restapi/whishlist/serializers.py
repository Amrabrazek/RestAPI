from rest_framework import serializers
from .models import Whishlist

# class WhishlistSerializer(serializers.ModelSerializer):
#     user = serializers.PrimaryKeyRelatedField(read_only=True)
#     product = serializers.PrimaryKeyRelatedField(read_only=True)

#     class Meta:
#         model = Whishlist
#         fields = '__all__'




class WhishlistSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'user', 'product')
        model = Whishlist