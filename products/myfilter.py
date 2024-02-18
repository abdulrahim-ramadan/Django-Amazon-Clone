from django_filters import rest_framework as filters

from .models import Product


class CustomProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name' : ['contains'],
            'brand' : ['exact'],
            'flag' : ['exact'],
            'price' : ['range']
        }