""" This file is used to define the URL patterns for the goods app. """

from django.urls import path
from goods import views

app_name = "goods"

urlpatterns = [
    path("", views.catalog, name="index"),
    path("product/", views.product, name="product"),
]
