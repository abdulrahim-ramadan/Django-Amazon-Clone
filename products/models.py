from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.utils.text import slugify



FLAG_CHOICES = (
    ('New','New'),
    ('Sale','Sale'),
    ('Feature','Feature'),
)



class Product(models.Model):
    name = models.CharField(_('Product Name'),max_length=120)
    image =models.ImageField(_('Image'),upload_to='products')
    price =models.FloatField(_('Price'))
    subtitle = models.TextField(_('Subtitle'),max_length=500)
    description = models.TextField(_('Description'),max_length=50000)
    sku = models.IntegerField(_('SKU'))
    video = models.URLField(_('Video'),null=True,blank=True)
    quantity = models.IntegerField(_('Quantity'))
    flag = models.CharField(_('Flag'),max_length=10,choices=FLAG_CHOICES)
    brand = models.ForeignKey('Brand',related_name='product_brand',on_delete=models.SET_NULL,null=True)
    slug =models.SlugField(null=True,blank=True)

# slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)





class ProductImages(models.Model):
    product = models.ForeignKey(Product , related_name='product_image',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')



class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='brands')
    slug =models.SlugField(null=True,blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)

    def __str__(self):
        return self.name    

class Review(models.Model):
    user =models.ForeignKey(User,related_name='review_user',on_delete=models.SET_NULL,null=True,blank=True)
    product =models.ForeignKey(Product,related_name='review_product',on_delete=models.CASCADE)
    review = models.TextField(max_length=300)
    rate = models.IntegerField()
    created_at = models.DateTimeField(timezone.now)

    def __str__(self):
        return str(self.user)