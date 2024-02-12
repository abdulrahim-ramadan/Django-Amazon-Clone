from django.urls import path
from .views import ProductList,ProductDetail,BrandList,BrandDetail, add_product_review

from .api import  ProductListAPI,ProductDetailAPI
urlpatterns =[
    path('' , ProductList.as_view()),
    path('brands' , BrandList.as_view()),
    path('<slug:slug>', ProductDetail.as_view()),
    path('<slug:slug>/add-review', add_product_review),
    path('brands/<slug:slug>' , BrandDetail.as_view()),

    # path('api/list' , product_list_api),
    path('api/list', ProductListAPI.as_view(),name='product list api'),
    path('api/list/<int:pk>', ProductDetailAPI.as_view(),name='product detail api')
]