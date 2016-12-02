"""Serializadores da aplicação contato."""

from django.conf import settings
from django.core import mail
from rest_framework import serializers


class FormulárioContatoSerializer(serializers.Serializer):
    """Formulário de contato como serializador."""

    email = serializers.EmailField()
    subject = serializers.CharField()
    message = serializers.CharField()

    def save(self, *args, **kwargs):
        """Processa o formulário."""
        params = self.validated_data
        email, assunto, mensagem = params['email'], params['subject'], params['message']

        mail.send_mail(assunto, mensagem, email, [m[1] for m in settings.MANAGERS])
