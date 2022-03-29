from django import template
from django.utils.html import escape

import markdown as md

from marklichen.extensions import TaxonExtension

register = template.Library()

MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    TaxonExtension()
]


@register.filter
def markdown(value):
    escaped = escape(value)
    return md.markdown(escaped, extensions=MARKDOWN_EXTENSIONS)
