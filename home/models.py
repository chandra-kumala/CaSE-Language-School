from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import (
    StreamField,
)
from wagtail.admin.edit_handlers import (
    StreamFieldPanel,
)
from wagtail.search import index

from wagtools.snippet import Seo, Google, Facebook, SocialLinks
from wagtools.blocks import CommonStreamBlock


class HomePage(Page, Seo):
    my_stream = StreamField(CommonStreamBlock(required=False), null=True, blank=True)

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['menuitems'] = request.site.root_page.get_descendants(
            inclusive=True).live().in_menu()
        return context

    search_fields = Page.search_fields + [
        index.SearchField('my_stream'),
    ]

    content_panels = Page.content_panels + [
        StreamFieldPanel('my_stream', "Main content..."),
    ]
    promote_panels = Page.promote_panels + Seo.panels
