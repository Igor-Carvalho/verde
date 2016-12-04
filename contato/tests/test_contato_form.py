"""Módulo contento testes do formulário de contato."""

from django.conf import settings
from django.core import mail, urlresolvers
from django.test import override_settings
from rest_framework import status
from rest_framework.test import APITestCase

from .. import serializers


class TestContatoForm(APITestCase):
    """Testa o formulário de contato."""

    @classmethod
    def setUpClass(cls):
        """Class fixtures."""
        super().setUpClass()
        cls.formulário_url = urlresolvers.reverse('contato:enviar_formulário')

    def test_enviar_formulário(self):
        """Verifica se o formulário é enviado com sucesso."""
        self.assertEqual(len(mail.outbox), 0)
        params = dict(email='email@domain.com', subject='Assunto', message='Mensagem teste')
        response = self.client.post(self.formulário_url, params)
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(len(mail.outbox), 1)

        email = mail.outbox[0]
        self.assertEqual(email.from_email, settings.SERVER_EMAIL)
        self.assertEqual(email.subject, '{}{}'.format(settings.EMAIL_SUBJECT_PREFIX, 'Assunto'))
        serializer = serializers.FormulárioContatoSerializer(data=params)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(email.body, serializer.construir_mensagem_de_email())
        self.assertEqual(email.to, [m[-1] for m in settings.MANAGERS])

    def test_enviar_formulário_bad_request(self):
        """Verifica se mensagens de erro são enviadas corretamente ao usuário."""
        response = self.client.post(self.formulário_url, dict())
        self.assertTrue(status.is_client_error(response.status_code))
        self.assertEqual(response.data['email'][0], 'Este campo é obrigatório.')
        self.assertEqual(response.data['subject'][0], 'Este campo é obrigatório.')
        self.assertEqual(response.data['message'][0], 'Este campo é obrigatório.')

    @override_settings(
        EMAIL_BACKEND='django.core.mail.backends.filebased.EmailBackend',
        EMAIL_FILE_PATH='/',
    )
    def test_enviar_formulário_server_error(self):
        """Verifica se é enviado ao cliente um http 500 em cada de erro no servidor."""
        with self.assertRaises(Exception):
            params = dict(email='email@domain.com', subject='Assunto', message='Mensagem teste')
            self.client.post(self.formulário_url, params)
