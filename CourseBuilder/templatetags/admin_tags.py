# templatetags/tag_library.py

from django import template

register = template.Library()

@register.filter()
def to_int(value):
    return int(value)

@register.filter()
def form_num_prefix(value):
    return value.split('-')[1]