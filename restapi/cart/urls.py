from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    
    # ________________________________________ Django Cart Task ____________________________
    path('api/add_to_cart/<int:user_id>', views.add_to_cart_api, name="add_to_cart_api"),
    path('api/get_cart/<int:user_id>', views.get_cart_api, name="get_cart_api"),
    path('api/get_cart/<int:user_id>/<int:product_id>', views.get_cart_api, name='delete-cart-product-api'),
    
]