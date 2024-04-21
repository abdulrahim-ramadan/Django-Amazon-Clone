from django.shortcuts import render , redirect
from django.views.generic import ListView , DetailView 

from django.db.models import Q , F , Func , DecimalField , Value , CharField
from django.db.models.aggregates import Avg , Sum , Count , Max , Min

from .models import Product , Brand , Review , ProductImages
from .forms import ReviewForm

from django.db.models.functions import Cast
from django.views.decorators.cache import cache_page



@cache_page(60 * 1)
def debug(request):
    # data = Product.objects.all()

    # data = Product.objects.filter(price__gt=98)
    # data = Product.objects.filter(price__gte=98)
    # data = Product.objects.filter(price__lt=22)
    # data = Product.objects.filter(price__lte=22)
    # data = Product.objects.filter(price__range=(21,22))

    # data = Product.objects.filter(name__contains='Jeffrey')
    # data = Product.objects.filter(name__startswith='Jeffrey')
    # data = Product.objects.filter(name__endswith='Garcia')

    # data = Product.objects.filter(name__contains='Jeffrey',price__gt=50)
    
    # data = Product.objects.filter(
    #     Q(name__contains='Jeffrey') &
    #     Q(price__gt=90)
    #       )

    # data = Product.objects.filter(
    #     Q(name__contains='Jeffrey') |
    #     Q(price__gt=50)
    #       )
    
    # data = Product.objects.filter(
    #     Q(name__contains='Jeffrey') |
    #     ~Q(price__gt=22)
    #       )

    # data = Product.objects.order_by('price')
    # data = Product.objects.order_by('-price')
    
    # data = Product.objects.all()[:5]
    # data = Product.objects.earliest('price')
    # data = Product.objects.latest('price')
    # print(data)

    # django queries are lazy
    # data = Product.objects.filter(name__contains='Jeffrey').order_by('-price')      # merg queries (SQl)

    # data = Product.objects.filter(name__contains='Jeffrey')
    # data = data.order_by('-price')

    # data = Product.objects.all()
    # data = Product.objects.values('name')
    # # data = Product.objects.values_list('name')
    # data = Product.objects.only('name')
    # data = Product.objects.defer('slug','description')

    # data = Product.objects.all() # R product:brand
    # data = Product.objects.select_related('brand').all() # products:brands one table Foreignkey ,one-to-one
    # data = Product.objects.prefetch_related('brand').all() # many-to-many

    # aggregation
    # data = Product.objects.aggregate(myavg=Avg('price'))
    # data = Product.objects.aggregate(mysum=Sum('price'))
    # data = Product.objects.aggregate(mymin=Min('price'))
    # data = Product.objects.aggregate(mymax=Max('price'))

    #Annotation
    # data = Product.objects.annotate(sell_price=F('price')*1.20)
    # data = Product.objects.annotate(
    # sell_price=Func(F('price') *1.20 , function='ROUND')
    ## )

    data = Product.objects.all()


    return render(request,'products/debug.html',{'data':data})



class ProductList(ListView):
    model = Product
    paginate_by = 50




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
    paginate_by = 20

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