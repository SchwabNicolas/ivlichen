"""ivlichen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from ivlichen.views import TaxonCreateView, TaxaListView, IndexView, ObservationCreateView, TaxonAutocomplete, TaxonDetailView, TaxonUpdateView

from ivlichen.ivlichen import settings

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('index/', IndexView.as_view(), name='index'),

    path('create-taxon/', TaxonCreateView.as_view(), name='create-taxon'),
    path('taxon-detail/<slug:slug>', TaxonDetailView.as_view(), name='taxon-detail'),
    path('taxon-update/<slug:slug>', TaxonUpdateView.as_view(), name='taxon-update'),
    path('list-taxa/', TaxaListView.as_view(), name='list-taxa'),

    path('create-observation/', ObservationCreateView.as_view(), name='create-observation'),

    re_path(r'^synonym-autocomplete/$', TaxonAutocomplete.as_view(), name='taxon-autocomplete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
