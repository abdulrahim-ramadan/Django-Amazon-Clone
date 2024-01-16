from django.shortcuts import render
from django.views.generic import ListView , DeleteView

from .models import Product , Brand , Review

# Create your views here.
class ProductList(ListView):
    model = Product



class ProductDetail(DeleteView):
    model = Product



class BrandList(ListView):
    model = Brand


class BrandDetail(DeleteView):
    model = Brand
