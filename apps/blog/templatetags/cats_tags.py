from django import template
from ..models import *

register = template.Library()


@register.simple_tag()
def getcats():
    return Category.objects.all()
