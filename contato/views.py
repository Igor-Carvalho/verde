"""Views da aplicação contato."""

from django.views import generic
from rest_framework import generics

from . import serializers


class ContatoView(generic.TemplateView):
    """Página de contato."""

    template_name = 'contato/contato.html'


contato_view = ContatoView.as_view()


class ContatoFormView(generic.TemplateView):
    """Server side partial para o formulário de contato."""

    template_name = 'contato/form.html'


contato_form_view = ContatoFormView.as_view()


class EnviarFormulárioView(generics.CreateAPIView):
    """Processa o formulário de contato."""

    serializer_class = serializers.FormulárioContatoSerializer


enviar_formulário_view = EnviarFormulárioView.as_view()
