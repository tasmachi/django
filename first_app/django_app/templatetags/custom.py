from django import template

register=template.Library()

@register.filter(name='cutten')
def cutten(value,arg):
    return value.replace(arg,'')