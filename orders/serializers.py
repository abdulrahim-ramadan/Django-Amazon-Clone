from rest_framework import serializers
from .models import Cart , CartDetail , Order , OrderDetail


class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartDetail
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    cart_detail = CartDetailSerializer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = '__all__' 


class OrderSerializer(serializers.ModelSerializer):
    OrderDetail = OrderDetailSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'               