from django.db import models
from django.db.models import Model
from django.utils import timezone


class Taxon(Model):
    TROPHIC_MODE = [
        ('lich', 'Lichen'),
        ('lich_fun', 'Champignon lichénicole'),
    ]

    name = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    publication_year = models.CharField(max_length=50)
    icn_identifier = models.IntegerField()
    cover_image = models.ForeignKey('Image', on_delete=models.CASCADE, null=True, default=None)
    trophic_mode = models.CharField(choices=TROPHIC_MODE, max_length=25, default='Lichen')


class Image(Model):
    image = models.ImageField('taximg/')
    legend = models.CharField(max_length=125, null=True, default=None)


class Observation(Model):
    taxon = models.ForeignKey('Taxon', models.CASCADE)
    images = models.ManyToManyField('Image')
    date = models.DateField(default=timezone.now)
    locality = models.CharField(max_length=125, null=True, default=None)
