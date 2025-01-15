"""Goods app views"""

from django.shortcuts import render

import goods
from goods.models import Products


def catalog(request):
    """Catalog page view"""
    goods = Products.objects.all()

    context = {
        "title": "Home - Каталог",
        "goods": goods,          
    }

    return render(request, "goods/catalog.html", context)


def product(request):
    """Product page view"""
    return render(request, "goods/product.html")

