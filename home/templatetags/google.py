from django import template
from home.models import Google

register = template.Library()

# Google snippets
@register.simple_tag
def google_tag():
    return Google.objects.first().site_tag