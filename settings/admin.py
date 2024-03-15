from django.contrib import admin

# Register your models here.

from .models import Company , DelveryFee

admin.site.register(Company)
admin.site.register(DelveryFee)
