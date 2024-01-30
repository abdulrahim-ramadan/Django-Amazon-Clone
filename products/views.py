from django.shortcuts import render
from django.views.generic import ListView , DetailView

from .models import Product , Brand , Review ,ProductImages

# Create your views here.
class ProductList(ListView):
    model = Product



class ProductDetail(DetailView):
    model = Product



    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context["product_images"] = ProductImages.objects.filter(product=self.get_object())
        context['product_reviews'] = Review.objects.filter(product=self.get_object()) 
        return context
    



class BrandList(ListView):
    model = Brand


class BrandDetail(ListView):
    model = Product             # products ----)  # products
    template_name = 'products/brand_detail.html'


    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = super().get_queryset()    # all products
        queryset = queryset.filter(brand = brand)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug']) 
        return context


