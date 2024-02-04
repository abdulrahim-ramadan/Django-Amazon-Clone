from django.contrib import admin



from .models import Product , Brand , Review , ProductImages

class ProductImageInline(admin.TabularInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','flag','price']
    list_filter = ['flag','price','quantity']
    search_fields = ['name','subtitle','description']
    inlines = [ProductImageInline]


class ReviewAdmin(admin.ModelAdmin):
    list_display =['user','product','rate','created_at']
    list_filter =['rate','created_at']    

admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Review,ReviewAdmin)