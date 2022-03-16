from dal import autocomplete
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView

from ivlichen.forms import TaxonCreateUpdateForm, ObservationCreateUpdateForm
from ivlichen.models import Taxon


class IndexView(TemplateView):
    template_name = 'index.html'


class TaxonCreateView(CreateView):
    template_name = 'taxon/create.html'
    form_class = TaxonCreateUpdateForm
    success_url = reverse_lazy('index')


class ObservationCreateView(CreateView):
    template_name = 'observation/create.html'
    form_class = ObservationCreateUpdateForm
    success_url = reverse_lazy('index')


class TaxaListView(ListView):
    template_name = 'taxon/list.html'
    context_object_name = 'taxa'
    model = Taxon
    paginate_by = 100


class TaxonAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Taxon.objects.all().order_by('name')

        if self.q:
            qs = qs.filter(name__startswith=self.q)

        return qs
