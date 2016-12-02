"""Views da aplicação contato."""

from rest_framework import generics

from . import serializers


class EnviarFormulárioView(generics.CreateAPIView):
    """Processa o formulário de contato."""

    serializer_class = serializers.FormulárioContatoSerializer


enviar_formulário_view = EnviarFormulárioView.as_view()
