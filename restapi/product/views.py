from rest_framework import generics,permissions
from .models import Category, Product
from .serializers import CategorySerializer,ProductSerializer, ProductSerializer_2
from .permissions import IsAuthorOrReadOnly

# Create Admin views here.

class ListProducts_author(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny ,)

    serializer_class = ProductSerializer_2
    def get_queryset(self):
        owner_id = self.kwargs['pk']
        return Product.objects.filter(owner=owner_id)


    
class ListProductDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = ( IsAuthorOrReadOnly, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer_2



# Create Buyer views here.
class ListCategories(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ListProducts(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['pk']
        return Product.objects.filter(category__id=category_id)
    
class SingleProduct(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
