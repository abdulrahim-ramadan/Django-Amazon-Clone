from django.urls import path 
from .views import add_to_cart ,order_list,checkout,process_payment,payment_failed,payment_success
from .api import OrderDetailAPI , OrderListAPI , ApplyCouponAPI , CartCreateUpdateDeleteAPI , CreateOrderAPI


urlpatterns = [
    path('', order_list),
    path('checkout/', checkout),
    path('checkout/process_payment',process_payment ),
    path('checkout/payment/success',payment_success),
    path('checkout/payment/failed',payment_failed ),
    path('add-to-cart', add_to_cart),


    # api
    path('api/<str:username>', OrderListAPI.as_view()),
    path('api/<str:username>/<int:pk>', OrderDetailAPI.as_view()),
    path('api/<str:username>/<int:pk>', CreateOrderAPI.as_view()),
    path('api/<str:username>/cart', CartCreateUpdateDeleteAPI.as_view()),
    path('api/<str:username>/apply-coupon', ApplyCouponAPI.as_view()),

    
]