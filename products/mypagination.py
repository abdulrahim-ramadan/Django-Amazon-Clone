from rest_framework.pagination import  PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 20