from django import template
register = template.Library()


@register.filter
def indexof(list, i):
    return list.index(i)


