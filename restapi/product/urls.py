from django.urls import path
from product.views import ListProducts,ListCategories,SingleProduct

urlpatterns = [
    path('category/',ListCategories.as_view()),
    path('category_products/<int:pk>', ListProducts.as_view()),
    path('single_product/<int:pk>', SingleProduct.as_view() )
]