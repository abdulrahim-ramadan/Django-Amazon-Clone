from django.contrib import admin

from .models import Address , Profile , Phones


admin.site.register(Profile)
admin.site.register(Phones)
admin.site.register(Address)