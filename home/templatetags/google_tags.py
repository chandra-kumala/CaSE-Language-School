from django import template
from home.models import Google

register = template.Library()

# Google snippets
@register.inclusion_tag('home/tags/google.html', takes_context=True)
def google_tags(context):
    return {
        'google_tags': Google.objects.all(),
        'request': context['request'],
    }