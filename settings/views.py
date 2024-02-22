from django.shortcuts import render
from products.models import Product , Brand , Review

def  home (request):
    brands = Brand.objects.all()[:10]
    sale = Product.objects.filter(flag ='Sale')[:10]
    new = Product.objects.filter(flag ='New')[:10]
    feature = Product.objects.filter(flag ='Feature')[:6]
    review = Review.objects.filter(rate=5)[:3]


    return render(request, 'settings/home.html', {
        'brands' : brands,
        'sale': sale,
        'new' : new,
        'feature' : feature,
        'review' : review,
        
        })
