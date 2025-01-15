''' This file is used to create custom template tags for the goods app '''

from goods.models import Categories
from django import template

register = template.Library()

@register.simple_tag()
def tag_categories():
    ''' This function is used to return all the categories from the database '''
    return Categories.objects.all()
