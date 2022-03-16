import xml.etree.ElementTree as etree

from markdown import Extension
from markdown.inlinepatterns import DoubleTagInlineProcessor

from ivlichen.models import Taxon

TAXON_RE = r'\[\[(.*?)\]\]'


class TaxonInlineProcessor(DoubleTagInlineProcessor):
    def handleMatch(self, m, data):
        taxon = etree.Element('a')
        taxon.text = m.group(1)
        mg = m.group(1)

        tax = Taxon.objects.filter(name=mg)

        if tax.exists():
            tax = tax.first()

        if tax is not None:
            taxon.set('title', f'Voir la fiche de {taxon.text}')
            taxon.set('href', tax.get_absolute_url())
            taxon.set('class', 'text-amazon-50 italic')
        else:
            taxon.set('title', f'Fiche introuvable pour {mg}')
            taxon.set('href', '#')
            taxon.set('class', 'text-red-50 italic')
        return taxon, m.start(0), m.end(0)


class TaxonExtension(Extension):
    def extendMarkdown(self, md):
        md.inlinePatterns.register(TaxonInlineProcessor(TAXON_RE, md), 'taxon', 175)
