from django.db import models
from django.db.models import Model
from django.utils import timezone

from marklichen.models import MarkdownField


class Taxon(Model):
    TROPHIC_MODE = [
        ('lich', 'lichen'),
        ('lich_fun', 'champignon lichénicole'),
    ]

    SHAPE = [
        ('crust', 'crustacé'),
        ('lepr', 'lépreux'),
        ('comp', 'composé'),
        ('fol', 'foliacé'),
        ('frut', 'fruticuleux'),
        ('squa', 'squamuleux'),
        ('gel', 'gélatineux'),
        ('other', 'autre'),
    ]

    DIVISIONS = [
        ('asco', 'Ascomycota'),
        ('basidio', 'Basidiomycota'),
    ]

    name = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    publication_year = models.CharField(max_length=50)
    icn_identifier = models.IntegerField()
    family = models.CharField(max_length=100, null=True, blank=True, default='')
    division = models.CharField(choices=DIVISIONS, max_length=10, default='asco')
    cover_image = models.ForeignKey('Image', on_delete=models.CASCADE, null=True, blank=True, default=None)
    trophic_mode = models.CharField(choices=TROPHIC_MODE, max_length=25, default='lich')
    shape = models.CharField(choices=SHAPE, max_length=25, default='crust')
    remarks = MarkdownField(max_length=1000, null=True, blank=True, default='')

    def __str__(self):
        return self.name


class Image(Model):
    image = models.ImageField('taximg/')
    legend = models.CharField(max_length=125, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)


class Observation(Model):
    SUBSTRATE = [
        ('epi', 'épiphyte'),
        ('sax', 'saxicole'),
        ('cort', 'corticole'),
        ('terr', 'terricole'),
        ('musc', 'muscicole'),
        ('lich', 'lichénicole'),
    ]

    taxon = models.ForeignKey('Taxon', models.CASCADE)
    date = models.DateField(default=timezone.now)
    locality = models.CharField(max_length=125, null=True, blank=True, default="")
    substrate = models.CharField(choices=SUBSTRATE, max_length=5, default='epi')
    host = models.CharField(max_length=150, null=True, blank=True)
    outside_scope = models.BooleanField(default=False)
    images = models.ManyToManyField('Image')
