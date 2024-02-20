from django.shortcuts import render ,redirect
from django.views.generic import ListView , DetailView 

from django.db.models import Q 

from .models import Product , Brand , Review , ProductImages
from .forms import ReviewForm

def  debug(requset):
    #data = Product.objects.defer()
    #data = Product.objects.filter(price__gt=98)
    #data = Product.objects.filter(price__gte=98)
    #data = Product.objects.filter(price__lt=22)
    #data = Product.objects.filter(price__lte=22)
    #data = Product.objects.filter(price__range=(21,22))


    #data = Product.objects.filter(name__contains='Jeffrey')
    #data = Product.objects.filter(name__startswith='Jeffrey')
    #data = Product.objects.filter(name__endswith='Garcia')

#1
    #data = Product.objects.filter(name__contains='Jeffrey',price__gt=50)

#2
    # data = Product.objects.filter(
    #      Q(name__contains='Jeffrey') &
    #      Q(price__gt=50)
    #        )



    # data = Product.objects.filter(
    #      Q(name__contains='Jeffrey') |
    #      Q(price__gt=90)
    #        )    


    # data = Product.objects.filter(
    #      Q(name__contains='Jeffrey') |
    #      ~Q(price__gt=22)
    #        )    



    #data = Product.objects.order_by('price')
    #data = Product.objects.order_by('-price')

    #data = Product.objects.all()[:5]
    #data = Product.objects.earliest('price')
    # data = Product.objects.latest('price')
    #print(data)

    # django queries are lazy ........(1 tast !).......
    #data = Product.objects.filter(name__contains='Jeffrey').order_by('-price')      # merg queries (SQl)

    # django queries are lazy 2 
    #data = Product.objects.filter(name__contains='Jeffrey')
    #data=data.order_by('-price')


    # data = Product.objects.all()
    #data = Product.objects.values('name')
    #data = Product.objects.values_list('name')
    #data = Product.objects.only('name') 

    data = Product.objects.defer('slug','description')     


    return render(requset,'products/debug.html',{'data':data})


class ProductList(ListView):
    model = Product
    


'''
    1: product detail:
        -base funtion : get_queryset
        - extra data : get_context_data
'''




class ProductDetail(DetailView):
    model = Product


    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_images"] = ProductImages.objects.filter(product=self.get_object())
        context["product_review"] = Review.objects.filter(product=self.get_object())
        return context




class BrandList(ListView):
    model = Brand
    paginate_by = 20


class BrandDetail(ListView):
    model = Product
    template_name = 'products/brand_detail.html' 

    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = super().get_queryset()
        queryset = queryset.filter(brand=brand)
        return queryset 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['brand'] = Brand.objects.get(slug=self.kwargs['slug'])
        return context
    

def add_product_review(request,slug):
    product = Product.objects.get(slug=slug)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user =  request.user
            myform.product = product
            myform.save()

            return redirect(f'/products/{slug}')
    