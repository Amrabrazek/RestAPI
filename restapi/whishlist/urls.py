from django.urls import path

from .views import wishList, wishListDetail

urlpatterns = [
path('', wishList.as_view()),
path('<int:pk>/', wishListDetail.as_view()),

]