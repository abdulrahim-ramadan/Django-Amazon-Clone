from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from products.models import Product
from accounts.models import Address
from utils.generate_code import generate_code

from settings.models import DeliveryFee



ORDER_STATUS = (
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered')
)


class Order(models.Model):
    user = models.ForeignKey(User,related_name='order_user',on_delete=models.SET_NULL,null=True,blank=True)
    order_code = models.CharField(max_length=10,default=generate_code)
    status = models.CharField(max_length=15,choices=ORDER_STATUS)
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(null=True,blank=True)
    delivery_location = models.ForeignKey(Address,related_name='delivery_address',on_delete=models.SET_NULL,blank=True, null=True)
    coupon = models.ForeignKey('Coupon',related_name='order_coupon',on_delete=models.SET_NULL,blank=True,null=True)
    order_total_discount = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.user)
    
# coupon code 3 
    

    def order_sub_total(self):
        if self.coupon:
            return self.order_total_discount
        
        total = 0
        for item in self.order_detait.all():
            total += item.total
        return total
    
    def order_total(self):
        fee = DeliveryFee.objects.last().fee
        return self.order_sub_total() + fee
    
    def order_discount(self):
        if self.coupon:
            after_discount = self.order_sub_total()

            before_discount = 0
            for item in self.order_detail.all():
                before_discount += item.total
            return before_discount - after_discount
    
        else:
            return 0
        
    




class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name='order_detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_product',on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return str(self.order)

CART_STATUS = (
    ('InProgress','InProgress'),
    ('Completed','Completed'),
)


class Cart(models.Model):
    user = models.ForeignKey(User,related_name='cart_user',on_delete=models.SET_NULL,null=True,blank=True)
    status = models.CharField(max_length=15,choices=CART_STATUS)
    coupon = models.ForeignKey('Coupon',related_name='cart_coupon',on_delete=models.SET_NULL,blank=True,null=True)
    order_total_discount = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.user)
    
    def cart_total(self):
        
        total = 0
        for item in self.cart_detail.all():
            total += item.total

        return total
    



    def cart_discount(self):
        if self.coupon:
            after_discount = self.order_total_discount

            before_discount = 0
            for item in self.cart_detail.all():
                before_discount += item.total
            return round(before_discount - after_discount,2)
        
        else:
            return 0
        

        

class CartDetail(models.Model):
    cart = models.ForeignKey(Cart,related_name='cart_detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='cart_product',on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=1)
    total = models.FloatField(default=0)

    def __str__(self):
        return str(self.cart)


class Coupon(models.Model):
    code = models.CharField(max_length=20)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    quantity = models.IntegerField()
    discount = models.FloatField()

    def __str__(self):
        return self.code