from django.shortcuts import render

# Create your views here.
from rest_framework import generics,permissions
from .models import Whishlist
from .serializers import WhishlistSerializer


class wishList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,) # new
    queryset = Whishlist.objects.all()
    serializer_class = WhishlistSerializer



class wishListDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,) # new
    queryset = Whishlist.objects.all()
    serializer_class = WhishlistSerializer