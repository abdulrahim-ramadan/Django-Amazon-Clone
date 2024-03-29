from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import Cart , CartDetail , Order , OrderDetail , Coupon
from .serializers import CartSerializer , CartDetailSerializer , OrderSerializer , OrderDetailSerializer

from settings.models import DeliveryFee
from products.models import Product



class OrderListAPI(generics.ListAPIView):
    pass
    


class OrderDetailAPI(generics.RetrieveAPIView):
    pass
    


class CreateOrderAPI(generics.GenericAPIView):
    pass



class ApplyCouponAPI(generics.GenericAPIView):
    pass



class CartCreateUpdateDeleteAPI(generics.GenericAPIView):
    pass

