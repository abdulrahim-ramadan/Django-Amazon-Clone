from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

from .serializers import ProductListSerializer , ProductDetailSerializers , BrandListSerialzer , BrandDetailSerialzer
from.models import Product , Brand 
from .mypagination import CustomPagination
from .myfilter import CustomProductFilter




# @api_view(['GET'])
# def product_list_api(request):
#     products = Product.objects.all()
#     data = ProductSerializer(products,many=True,context={"request":request}).data
#     return Response({'products':data})



class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['flag', 'brand', 'quantity']
    # search_fields = ['name', 'subtitle','description']
    ordering_fields = ['price', 'quantity', 'name']
    filterset_class = CustomProductFilter
    permission_classes = [IsAuthenticated]


class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers
    permission_classes = [IsAuthenticated]

class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerialzer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

class BrandDetailAPI(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerialzer         
