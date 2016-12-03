"""Módulo contém views genéricas ou globais ao projeto."""

from django.core import urlresolvers
from django.views import generic


class RedirectIndexView(generic.RedirectView):
    """Redireciona para home."""

    url = urlresolvers.reverse_lazy('home')
    permanent = True


redirect_index_view = RedirectIndexView.as_view()


class IndexView(generic.TemplateView):
    """
    Página base da aplicação.

    Esta página contém a infraestrutura SPA (Single Page Application): scripts, estilos, etc.
    """

    template_name = 'base.html'


index_view = IndexView.as_view()


class SobreView(generic.TemplateView):
    """Página sobre a empresa."""

    template_name = 'sobre.html'


sobre_view = SobreView.as_view()
