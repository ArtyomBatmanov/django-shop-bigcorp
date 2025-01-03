from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, ProductProxy, Product


def products_list_view(request):
    products = Product.objects.all()
    return render(request, "shop/products.html", {"products": products})


def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "shop/product_detail.html", {"product": product})


def category_list_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.select_related("category").filter(category=category)
    context = {"category": category, "products": products}
    return render(request, "shop/category_list.html", context)

# Create your views here.
