""" This file is used to create custom template tags for the goods app """

from urllib.parse import urlencode
from goods.models import Categories
from django import template

register = template.Library()


@register.simple_tag()
def tag_categories():
    """This function is used to return all the categories from the database"""
    return Categories.objects.all()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    """This function is used to change the query parameters in the url"""

    query = context["request"].GET.dict()
    query.update(kwargs)
    return urlencode(query)
