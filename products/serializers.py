# Form:data --) JSON

from rest_framework import serializers
from .models import Product , Brand , Review , ProductImages

class BrandSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'        

class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    
    class Meta:
        model = Product
        fields = '__all__'


