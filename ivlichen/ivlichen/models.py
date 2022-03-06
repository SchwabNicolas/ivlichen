from django.db import models
from django.db.models import Model


class Species(Model):
    name = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    publication_year = models.CharField(max_length=50)
    cover_image = models.ForeignKey('Image', on_delete=models.CASCADE)


class Image(Model):
    image = models.ImageField('taximg/')
    legend = models.CharField(max_length=125)


class Observation(Model):
    taxon = models.ForeignKey('Species', models.CASCADE)
    images = models.ManyToManyField('Image', models.CASCADE)
