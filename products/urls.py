from django.urls import path
from .views import ProductList,ProductDetail,BrandList,BrandDetail, add_product_review


urlpatterns =[
    path('' , ProductList.as_view()),
    path('brands' , BrandList.as_view()),
    path('<slug:slug>', ProductDetail.as_view()),
    path('<slug:slug>/add-review',add_product_review),
    path('brands/<slug:slug>', BrandDetail.as_view()),
]