from django.shortcuts import get_object_or_404, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# ------------------ Django Task ------------------
from .models import Cart
from user.models import User
from product.models import Product
from .serializers import CartSerializer

# Create your views here.
class AddToCartAPIView(APIView):
    @permission_classes([IsAuthenticated])
    def post(self, request, user_id):
        data = {}
        try:
            user = get_object_or_404(User, id=user_id)
            product_id = request.data.get('product') # to get the product id from the request
            quantity = request.data.get('quantity') # to get the quantity from the request 

            if product_id is None or quantity is None:
                return Response({'error': 'Product ID and quantity are required.'}, status=status.HTTP_400_BAD_REQUEST)

            product = get_object_or_404(Product, id=product_id)
            cart_item, created = Cart.objects.get_or_create(user=user, product=product)
            if int(quantity) <= 0:
                return Response({'error': 'Quantity must be a positive number.'}, status=status.HTTP_400_BAD_REQUEST)

            if cart_item.quantity + int(quantity) > product.instock:
                return Response({'error': 'Requested quantity exceeds available quantity.'}, status=status.HTTP_400_BAD_REQUEST)

            # Update the quantity if the cart item already exists
            if not created:
                cart_item.quantity += int(quantity)
                cart_item.save()

            cart_serializer = CartSerializer(cart_item)
            data = cart_serializer.data
            http_status = status.HTTP_201_CREATED

        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f'exception in add_to_cart_api => {e}')
            data = {'error': 'Error occurred while adding item to cart.'}
            http_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(data=data, status=http_status)


class GetCartAPIView(APIView):
    @permission_classes([IsAuthenticated])
    def get(self, request, user_id, product_id=None):
        data = {}
        try:
            user = get_object_or_404(User, id=user_id)
            if product_id is not None:
                cart_item = get_object_or_404(Cart, user=user, product_id=product_id)
                cart_serializer = CartSerializer(cart_item)
                data = cart_serializer.data
                http_status = status.HTTP_200_OK
            else:
                cart_items = Cart.objects.filter(user=user)
                cart_serializer = CartSerializer(cart_items, many=True)
                data = cart_serializer.data
                http_status = status.HTTP_200_OK

        except Exception as e:
            print(f'exception in get_cart_api => {e}')
            http_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(data=data, status=http_status)

    @permission_classes([IsAuthenticated])
    def put(self, request, user_id, product_id=None):
        data = {}
        try:
            user = get_object_or_404(User, id=user_id)
            product = get_object_or_404(Product, id=product_id)
            cart_item = get_object_or_404(Cart, user=user, product=product)
            cart_serializer = CartSerializer(instance=cart_item, data=request.data, partial=True)
            if cart_serializer.is_valid():
                cart_serializer.save()
                data = cart_serializer.data
                http_status = status.HTTP_200_OK
            else:
                return Response(cart_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(f'exception in get_cart_api => {e}')
            http_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(data=data, status=http_status)

    @permission_classes([IsAuthenticated])
    def delete(self, request, user_id, product_id=None):
        data = {}
        try:
            user = get_object_or_404(User, id=user_id)
            if product_id is not None:
                product = get_object_or_404(Product, id=product_id)
                cart_item = get_object_or_404(Cart, user=user, product=product)
                cart_item.delete()
                send_cart_deleted_email(user)
            else:
                cart_items = Cart.objects.filter(user=user)
                cart_items.delete()
                send_cart_deleted_email(user)
            http_status = status.HTTP_204_NO_CONTENT

        except Exception as e:
            print(f'exception in get_cart_api => {e}')
            http_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(data=data, status=http_status)


def send_cart_deleted_email(user):
    subject = 'Cart Deleted'
    message = 'Your cart has been deleted.'
    recipient_list = [user.email]

    send_mail(subject, message, 'sender@example.com', recipient_list, fail_silently=False)
