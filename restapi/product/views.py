from rest_framework import generics
from .models import Category, Product
from .serializers import CategorySerializer,ProductSerializer
# Create Admin views here.












# Create Buyer views here.
class ListCategories(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ListProducts(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['pk']
        return Product.objects.filter(category__id=category_id)
    
class SingleProduct(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer