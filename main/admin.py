''' This file is used to register the models in the admin panel. '''
from django.contrib import admin

from goods.models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    """Products admin"""
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    """Categories admin"""
    prepopulated_fields = {"slug": ("name",)}
