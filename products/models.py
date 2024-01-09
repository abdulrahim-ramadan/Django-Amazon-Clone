from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


FLAG_CHOICES = (
    ('New','New')
    ('Sale','Sale')
    ('Feature','Feature')
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





class ProductImages(models.Model):
    pass



class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='brands')



class Review(models.Model):
    user =''
    Product =''
    Review = models.TextField(max_length=300)
    rate = models.IntegerField()
    created_at = models.DateTimeField(timezone.now)