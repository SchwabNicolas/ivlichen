from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView

from ivlichen.forms import TaxonCreateUpdateForm
from ivlichen.models import Taxon


class IndexView(TemplateView):
    template_name = 'index.html'


class TaxonCreateView(CreateView):
    template_name = 'taxon/create.html'
    form_class = TaxonCreateUpdateForm
    success_url = reverse_lazy('index')


class TaxaListView(ListView):
    template_name = 'taxon/list.html'
    context_object_name = 'taxa'
    model = Taxon
    paginate_by = 100


