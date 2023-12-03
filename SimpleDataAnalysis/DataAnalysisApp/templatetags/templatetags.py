from django import template
register = template.Library()

@register.filter
def index(List, i):
    return List[int(i)]

@register.filter
def key(Dict, i):
    return Dict[f"{i}"]