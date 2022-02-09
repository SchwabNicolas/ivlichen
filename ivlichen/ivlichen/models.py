from django.db import models
from django.db.models import Model


class Taxon(Model):
    name = models.ForeignKey('Name', on_delete=models.CASCADE)
    cover_image = models.ForeignKey('Image', on_delete=models.CASCADE)


class Name(Model):
    name = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    publication_year = models.CharField(max_length=50)


class Image(Model):
    image = models.ImageField('/media/taximg/')


class Observation(Model):
    taxon = models.ForeignKey('Taxon', models.CASCADE)
    images = models.OneTo('Image', models.CASCADE)
