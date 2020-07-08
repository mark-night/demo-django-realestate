from django import template
from django.http import QueryDict


register = template.Library()


@register.simple_tag(takes_context=True)
def update_query(context, key, value):
    queries = QueryDict(context.request.META.get('QUERY_STRING'), mutable=True)
    queries.__setitem__(key, value)
    return queries.urlencode()
