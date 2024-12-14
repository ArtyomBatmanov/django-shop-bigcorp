from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, ProductProxy, Product

def products_list_view(request):
    products = ProductProxy.objects.all()
    return render(request, "shop/products.html", {"products": products})




# Create your views here.
