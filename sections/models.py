from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.search import index

from home.models import CommonStreamBlock,  Seo

class SectionIndexPage(Page, Seo):
    alt_template = models.BooleanField(verbose_name="Use list style Index page instead?")
    my_stream = StreamField(CommonStreamBlock(), null=True, blank=True)

    def get_template(self, request):
        if self.alt_template:
            return 'sections/list_index_page.html'

        return 'sections/section_index_page.html'

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        context['menuitems'] = request.site.root_page.get_descendants(
            inclusive=True).live().in_menu()
        return context

    content_panels = Page.content_panels + [
        FieldPanel('alt_template'),
        StreamFieldPanel('my_stream')
    ]


class SectionPage(Page, Seo):
    date = models.DateField("Post date", null=True)
    body = RichTextField(blank=True)
    my_stream = StreamField(CommonStreamBlock(), null=True, blank=True,)

    parent_page_types = ['sections.SectionIndexPage', 'sections.ListIndexPage']

    def get_context(self, request):
        context = super(SectionPage, self).get_context(request)
        context['menuitems'] = request.site.root_page.get_descendants(
            inclusive=True).live().in_menu()

        return context

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.SearchField('my_stream'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body', classname="full"),
        StreamFieldPanel('my_stream'),
    ]

class ListIndexPage(SectionIndexPage):
    template = 'sections/list_index_page.html'