from django.shortcuts import render , redirect
from .models import Cart , CartDetail
from products.models import Product
from settings.models import DeliveryFee
from .models import Order , OrderDetail , Cart , CartDetail , Coupon
import datetime
from django.conf import settings

from django.http import JsonResponse
from django.template.loader import render_to_string
import stripe

from utils.generate_code import generate_code

def order_list(request):
    data = Order.objects.filter(user=request.user)
    delivery_fee = DeliveryFee.objects.last().fee
    return render(request,'orders/orders.html',{'orders':data , 'delivery_fee':delivery_fee})



def checkout(request):
    # review order , apply coupon

    cart = Cart.objects.get(user=request.user , status='InProgress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    delivery_fee = DeliveryFee.objects.last().fee
    discount = cart.cart_discount()
    sub_total = cart.cart_total()
    total = sub_total + delivery_fee
    pub_key = settings.STRIP_API_KEY_PUBLISHABLE

    # coupon code (BLACKFRIDAY)
    
    if request.method =='POST':
        code = request.POST['coupon_code']
        coupon = Coupon.objects.get(code=code)

        if coupon and coupon.quantity > 0:
            today = datetime.datetime.today().date()
            if today >= coupon.start_date and today <=coupon.end_date:
                coupon_value = sub_total /100*coupon.discount
                sub_total = sub_total - coupon_value
                total = sub_total + delivery_fee

                cart.coupon = coupon
                cart.order_total_discount = sub_total
                cart.save()


                return render(request,'orders/checkout.html',{
                'cart_detail':cart_detail ,
                'delivery_fee':delivery_fee ,
                'discount':coupon_value ,
                'sub_total':sub_total ,
                'total' :total ,
                'pub_key': pub_key

            })
        

    



    return render(request,'orders/checkout.html',{
        'cart_detail':cart_detail ,
        'delivery_fee':delivery_fee ,
        'discount':discount ,                # was ist das code 
        'sub_total':sub_total ,
        'total' :total,
        'pub_key': pub_key
    })
        


def process_payment(request):
    # process payment $
    
    cart = Cart.objects.get(user=request.user , status='InProgress')
    delivery_fee = DeliveryFee.objects.last().fee
    discount = cart.cart_discount()
    sub_total = cart.cart_total()
    total = sub_total + delivery_fee
    
    code = generate_code()
    
    # store code in session
    request.session['order_code'] = code
    request.session.save()
    
    stripe.api_key = settings.STRIPE_API_KEY_SECRET
    checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data':{
                        'currency': 'usd',
                        'product_data' : {'name':code},
                        'unit_amount': int(total*100)
                    },
                    'quantity':1
                },
            ],
            mode='payment',
            success_url='http://127.0.0.1:8000/orders/checkout/payment/success',
            cancel_url='http://127.0.0.1:8000/orders/checkout/payment/failed',
        )
    return JsonResponse({'session':checkout_session})


def payment_success(request):
    # if payment was success

    code = request.session.get('order_code')

    return render(request,'orders/success.html',{'code':code})


def payment_failed(request):
    # if payment was failed

    return render(request,'orders/failed.html',{})


def add_to_cart(request):
    product_id = request.POST['product_id']
    quantity = int(request.POST['quantity'])

    # get cart

    cart = Cart.objects.get(user=request.user , status='InProgress')

    # create cart detail

    product = Product.objects.get(id=product_id)
    cart_detail, created = CartDetail.objects.get_or_create(cart=cart,product=product)
    cart_detail.quantity = quantity
    cart_detail.total = round(quantity * product.price,2)
    cart_detail.save()
     
     # ajax code 

    cart = Cart.objects.get(user=request.user , status='InProgress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    
    total = cart.cart_total()           
    cart_count = len(cart_detail)
    
    page = render_to_string('cart.html',{'cart_data':cart , 'cart_detail_data':cart_detail})
    return JsonResponse({'result':page , 'total':total ,'cart_count' :cart_count})






