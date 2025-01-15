"""This file contains the views for the main app"""

from django.http import HttpResponse
from django.shortcuts import render
from django.template import context
from django.template.defaultfilters import first
from goods.models import Categories


def index(request):
    """Render the index page"""
    ctx = {
        "title": "Home-Главная",
        "content": "Магазин мебели HOME",
    }
    return render(request, "main/index.html", ctx)


def about(request):
    """Render the index page"""
    ctx = {
        "title": "Home-О нас",
        "content": "О нас",
        "text_on_page": "Текс о том почему этот магазин такой класный, и такой хоррший товар.",
    }
    return render(request, "main/about.html", ctx)
