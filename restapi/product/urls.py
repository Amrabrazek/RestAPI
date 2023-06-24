from django.urls import path
from product.views import ListProducts,ListCategories,SingleProduct,ListProducts_author, ListProductDetails

urlpatterns = [
    path('category/',ListCategories.as_view()),
    path('category_products/<int:pk>', ListProducts.as_view()),
    path('single_product/<int:pk>', SingleProduct.as_view() ),

    path('author_products/<int:pk>', ListProducts_author.as_view()),
    path('product/<int:pk>', ListProductDetails.as_view())

]
