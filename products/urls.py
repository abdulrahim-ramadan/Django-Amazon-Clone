from django.urls import path
from .views import ProductList,ProductDetail,BrandList,BrandDetail, add_product_review 

from .api import product_list_api , ProductListAPI

urlpatterns =[
    path('' , ProductList.as_view()),
    path('brands' , BrandList.as_view()),
    path('<slug:slug>', ProductDetail.as_view()),
    path('<slug:slug>/add-review',add_product_review),
    path('brands/<slug:slug>', BrandDetail.as_view()),


    path('api/list', product_list_api),
    path('api/list2', ProductListAPI.as_view())
]