
from django.shortcuts import render

# Create your views here.
from products.models import Product , Brand , Review # ----- dasboard
from orders.models import Order
from django.contrib.auth.models import User


def dashboard(request):

    products = Product.objects.all().count() #-----> dasboard data
    brands = Brand.objects.all().count()
    users = User.objects.all().count()
    orders = Order.objects.all().count()
    review = Review.objects.all().count()


    new_products = Product.objects.filter(flag='New').count()
    feature_products = Product.objects.filter(flag='Feature').count()
    sale_products = Product.objects.filter(flag='Sale').count()

    return render(request,'accounts/dashboard.html',{
        'products':products,
        'brands':brands,
        'users':users,
        'orders':orders,    #-----> dasboard data
        'review':review,
        'new_products': new_products,
        'feature_products': feature_products,
        'sale_products': sale_products
        
    })

def signup(request):
    pass    

def user_activate(request):
    pass
