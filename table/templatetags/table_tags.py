from django import template


register = template.Library()


@register.filter
def get_item(row, value):
    return row[value]