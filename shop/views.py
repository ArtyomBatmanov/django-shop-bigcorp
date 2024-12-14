from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, ProductProxy, Product

def products_list_view(request):
    products = ProductProxy.objects.all()
    return render(request, "shop/products.html", {"products": products})


def product_detail_view(request, slug):
    product = get_object_or_404(ProductProxy, slug=slug)
    return render(request, "shop/product_detail.html", {"product": product}

                  )

# Create your views here.
