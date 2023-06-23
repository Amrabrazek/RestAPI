from django.urls import path
from .views import AddToCartAPIView, GetCartAPIView

urlpatterns = [
    path('add-to-cart-api/<int:user_id>/', AddToCartAPIView.as_view(), name='add_to_cart_api'),
    path('get-cart-api/<int:user_id>/', GetCartAPIView.as_view(), name='get_cart_api'),
    path('get-cart-api/<int:user_id>/<int:product_id>/', GetCartAPIView.as_view(), name='get_cart_api'),
]