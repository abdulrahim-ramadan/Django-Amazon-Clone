from django.shortcuts import render , redirect
from .models import Cart , CartDetail
from products.models import Product
from settings.models import DeliveryFee
from .models import Order , OrderDetail , Cart , CartDetail , Coupon


def order_list(request):
    data = Order.objects.filter(user=request.user)
    return render(request,'orders/orders.html',{'orders':data})



def checkout(request):
    # review order , apply coupon

    cart = Cart.objects.get(user=request.user , status='InProgress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    delivery_fee = DeliveryFee.objects.last().fee
    discount = 0
    sub_total = cart.cart_total()
    total = sub_total + delivery_fee



    return render(request,'orders/checkout.html',{
        'cart_detail':cart_detail ,
        'delivery_fee':delivery_fee ,
        'discount':discount ,
        'sub_total':sub_total ,
        'total' :total
    })
        


def process_payment(request):
    # process payment $
    pass


def payment_success(request):
    # if payment was success

    code = ''

    return render(request,'orders/success.html',{})


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

    return redirect(f'/products/{product.slug}')
