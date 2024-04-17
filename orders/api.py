from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import Cart , CartDetail , Order , OrderDetail , Coupon
from .serializers import CartSerializer , CartDetailSerializer , OrderSerializer , OrderDetailSerializer

from settings.models import DeliveryFee
from products.models import Product
from accounts.models import Address
import datetime



class OrderListAPI(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

#get_queryset | get_context_data

# code 1 pro
    def get_queryset(self):
        queryset = super(OrderListAPI, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
    
#  code 2 ///
    # def list(self, request, *args, **kwargs):
    #     queryset = super().list(request, *args, **kwargs)
    #     queryset = queryset.filter(user=self.request.user)
    #     return queryset  
    


class OrderDetailAPI(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    


class CreateOrderAPI(generics.GenericAPIView):
    def post(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        code = request.data['payment_code']
        delivery_location = Address.objects.get(id=request.data['delivery_address_id'])

        cart = Cart.objects.get(user=user , status='InProgress')
        cart_detail = CartDetail.objects.filter(cart=cart)

        # create order from cart
        new_order = Order.objects.create(
            user = user ,
            order_code = code ,
            status = 'Recieved',
            delivery_location = delivery_location,
            coupon = cart.coupon ,
            order_total_discount = cart.order_total_discount
        )

        # cart order_details from cart_detail
        for object in cart_detail:
            OrderDetail.objects.create(
                order = new_order ,
                product = object.product ,
                quantity = object.quantity ,
                price = object.product.price ,
                total = object.quantity * object.product.price
            )

        cart.status = 'Completed'
        cart.save() 

        # send email : code 
        return Response({'message': 'Order was created successfuly'})



class ApplyCouponAPI(generics.GenericAPIView):
        def post(self,request,*args, **kwargs):
            user = User.objects.get(username=self.kwargs['username'])  #get user using username : url
            coupon = Coupon.objects.get(code = request.data['coupon_code']) #get coupon using coupon code comming from request body (mobile)
        
            cart = Cart.objects.get(user=user , status='InProgress')
            delivery_fee = DeliveryFee.objects.last().fee
            sub_total = cart.cart_total()
    


            if coupon and coupon.quantity > 0:
                today = datetime.datetime.today().date()
                if today >= coupon.start_date and today <= coupon.end_date:
                    coupon_value = sub_total /100*coupon.discount
                    sub_total = sub_total - coupon_value

                    cart.coupon = coupon
                    cart.order_total_discount = sub_total
                    cart.save()
                    return Response({'message':'coupon was applied successfully'})
                else:
                    return Response({'message':'coupon code date is not valid or expired'})
            
            else:
                return Response({'message':'coupon code not found or ended.. '})



class CartCreateUpdateDeleteAPI(generics.GenericAPIView):
    
    def get(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart , created = Cart.objects.get_or_create(user=user,status='InProgress')
        data = CartSerializer(cart).data
        return Response({'cart':data})

    def post(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])


    def delete(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        item_id = request.data['item_id']  # item id : delete

        product = CartDetail.objects.get(id=item_id)
        product.delete()

        #sand email
        
        return Response({'message':'item was deleted successfully'})

