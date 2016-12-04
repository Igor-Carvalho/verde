"""Serializadores da aplicação contato."""

from django.core import mail
from rest_framework import serializers


class FormulárioContatoSerializer(serializers.Serializer):
    """Formulário de contato como serializador."""

    email = serializers.EmailField()
    subject = serializers.CharField()
    message = serializers.CharField()

    def construir_mensagem_de_email(self):
        """Constroe a mensagem de email a ser enviada."""
        email, mensagem_original = self.validated_data['email'], self.validated_data['message']
        return '[Email Original: {}]\n\n{}'.format(email, mensagem_original)

    def save(self, *args, **kwargs):
        """Processa o formulário."""
        data = self.validated_data
        assunto, mensagem = data['subject'], self.construir_mensagem_de_email()

        mail.mail_managers(assunto, mensagem)
