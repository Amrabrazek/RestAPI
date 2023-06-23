from django.shortcuts import render

# Create your views here.
from rest_framework import generics,permissions
from .models import Whishlist
from .serializers import WhishlistSerializer


# class wishList(generics.ListAPIView):
#     # permission_classes = (permissions.IsAuthenticated,) # new
#     queryset = Whishlist.objects.all()
#     serializer_class = WhishlistSerializer



#based on user id get his wish list
class wishList(generics.ListAPIView):
    serializer_class = WhishlistSerializer
    # permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = Whishlist.objects.filter(user_id=user_id)
        return queryset




class wishListDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,) # new
    queryset = Whishlist.objects.all()
    serializer_class = WhishlistSerializer