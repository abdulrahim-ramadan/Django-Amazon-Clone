# Form:data --) JSON

from rest_framework import serializers
from .models import Product , Brand , Review , ProductImages

class BrandSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'  

class ProductImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImages
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'




class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    product_image = ProductImagesSerializer(many=True)
    review_product = ReviewSerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'


