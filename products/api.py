# views.py : API

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from .serializers import ProductSerializer
from .models import Product

#Functions
@api_view (['GET'])
def product_list_api(request):
    Products = Product.objects.all() # list
    data = ProductSerializer(Products,many=True,context={"request":request}).data # JSON
    return Response({'products':data})


class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
