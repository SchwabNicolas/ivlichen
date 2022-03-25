from dal import autocomplete
from django.forms import ModelForm, ImageField

from ivlichen.models import Taxon, Observation
from marklichen.widgets import SmallMarkdownWidget


class TaxonCreateUpdateForm(ModelForm):
    class Meta:
        model = Taxon
        fields = '__all__'
        exclude = [
            'cover_image'
        ]


class ObservationCreateUpdateForm(ModelForm):
    class Meta:
        model = Observation
        fields = '__all__'
        exclude = [
            'images',
        ]
        widgets = {
            'taxon': autocomplete.ModelSelect2(url='taxon-autocomplete'),
        }
