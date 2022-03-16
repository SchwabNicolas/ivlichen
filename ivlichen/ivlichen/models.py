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

    name = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    publication_year = models.CharField(max_length=50)
    icn_identifier = models.IntegerField()
    cover_image = models.ForeignKey('Image', on_delete=models.CASCADE, null=True, default=None)
    trophic_mode = models.CharField(choices=TROPHIC_MODE, max_length=25, default='lich')
    shape = models.CharField(choices=SHAPE, max_length=25, default='crust')
    remarks = MarkdownField(max_length=1000, null=True)


class Image(Model):
    image = models.ImageField('taximg/')
    legend = models.CharField(max_length=125, null=True, default=None)


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
    images = models.ManyToManyField('Image')
    date = models.DateField(default=timezone.now)
    locality = models.CharField(max_length=125, null=True, default=None)
    identifier = models.CharField(max_length=50, null=True)
    substrate = models.CharField()
    fine_substrate = MarkdownField(max_length=150, null=True)
