from django.db import models


from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail import blocks
from wagtail.admin.panels import FieldPanel

class StandardPage(Page):
    subtitle = models.CharField(max_length=250)
    # next, add the body, a rich text inside of a streamfield
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="title")),
        ('paragraph', blocks.RichTextBlock()),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
    ]