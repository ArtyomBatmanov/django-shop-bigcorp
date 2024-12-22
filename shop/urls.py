from django.urls import path, include
from .views import category_list_view, products_list_view, product_detail_view

app_name = "shop"

urlpatterns = [
    path("", products_list_view, name="products_list"),
    path("<slug:slug>/", product_detail_view, name="product_detail"),
    path("search/<slug:slug>/", category_list_view, name="category_list"),
]

