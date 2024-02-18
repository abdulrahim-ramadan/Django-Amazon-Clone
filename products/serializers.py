# Form:data --) JSON

from rest_framework import serializers
from .models import Product , Brand , Review , ProductImages

class BrandListSerialzer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()
    # count_name =serializers.SerializerMethodField(method_name='ramadan') 
    class Meta:
        model = Brand
        fields = '__all__' 

    def get_products_count(self,object) :
        count = object.product_brand.all().count()
        return count     

    # def ramadan()
    #   pass


class ProductImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImages
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'




class ProductListSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = '__all__'



class ProductDetailSerializers(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    product_images = ProductImagesSerializer(many=True)
    review_product = ReviewSerializer(many=True)
    review_count = serializers.SerializerMethodField()

    class Meta :
        model = Product
        fields = '__all__'

    def get_review_count (self, object):
        review_counts = object.review_product.all().count()
        return review_counts 


class BrandDetailSerializers(serializers.ModelSerializer):
    product_brand = ProductListSerializer(many=True)
    products_count = serializers.SerializerMethodField()
    class Meta :
        model = Brand
        fields = '__all__'




class BrandDetailSerialzer(serializers.ModelSerializer):
    product_brand = ProductListSerializer(many=True)
    
    products_count = serializers.SerializerMethodField()
    class Meta:
        model = Brand
        fields = '__all__'         
    
    
    def get_products_count(self,object) :
        count = object.product_brand.all().count()
        return count      







