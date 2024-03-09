from django.urls import path 
from .views import add_to_cart

urlpatterns = [
    path('add-to-cart', add_to_cart),
]