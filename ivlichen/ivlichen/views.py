from dal import autocomplete
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView

from ivlichen.forms import TaxonCreateUpdateForm, ObservationCreateUpdateForm
from ivlichen.models import Taxon, Image, Observation


class IndexView(TemplateView):
    template_name = 'index.html'


class TaxonCreateView(CreateView):
    template_name = 'taxon/create.html'
    form_class = TaxonCreateUpdateForm
    success_url = reverse_lazy('index')


class TaxonUpdateView(UpdateView):
    template_name = 'taxon/update.html'
    form_class = TaxonCreateUpdateForm
    context_object_name = 'taxon'
    model = Taxon
    success_url = reverse_lazy('index')


class TaxaListView(ListView):
    template_name = 'taxon/list.html'
    context_object_name = 'taxa'
    model = Taxon
    paginate_by = 100


class TaxonDetailView(DetailView):
    template_name = 'taxon/detail.html'
    context_object_name = 'taxon'
    model = Taxon

    def get_observations(self):
        return Observation.objects.filter(taxon=self.get_object())

    def get_list_coordinates(self):
        coordinates = []
        for observation in self.get_observations():
            if observation.latitude and observation.longitude is not None:
                coordinates.append([observation.date, observation.latitude, observation.longitude])
        return coordinates

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['taxon'] = self.get_object()
        context['coordinates'] = self.get_list_coordinates()
        context['observations'] = self.get_observations()
        return context


class ObservationCreateView(CreateView):
    template_name = 'observation/create.html'
    form_class = ObservationCreateUpdateForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        form = ObservationCreateUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            obs = form.save(*args, **kwargs)
            for file in request.FILES:
                obs.images.add(Image.objects.create(image=request.FILES[file]))
            return super().post(request, args, kwargs)
        return self.form_invalid(form)


class TaxonAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Taxon.objects.all().order_by('name')

        if self.q:
            qs = qs.filter(name__startswith=self.q)

        return qs
