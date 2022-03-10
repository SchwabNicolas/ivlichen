from django.forms import ModelForm

from ivlichen.models import Taxon


class TaxonCreateUpdateForm(ModelForm):
    class Meta:
        model = Taxon
        fields = '__all__'
        exclude = [
            'cover_image'
        ]
