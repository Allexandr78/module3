"""Goods app views"""

from django.shortcuts import render


def catalog(request):
    """Catalog page view"""
    return render(request, "goods/catalog.html")


def product(request):
    """Product page view"""
    return render(request, "goods/product.html")
