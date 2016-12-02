"""Testa adaptadores da aplicação core."""

import unittest

from django import urls
from django.core import urlresolvers
from django.test import SimpleTestCase, override_settings
from rest_framework.test import APITestCase


class DisableSignupAdapterTest(SimpleTestCase):
    """Verifica a suspensão de registro no site."""

    @override_settings(
        ACCOUNT_ADAPTER='core.adapters.DisableSignupAdapter',
        REST_AUTH_REGISTER_SERIALIZERS={
            'REGISTER_SERIALIZER': 'core.serializers.DisableSignupSerializer'
        }
    )
    def test_disable_signup(self):
        """Verifica se o processo de registro no site é suspenso."""
        try:
            url = urlresolvers.reverse('account_signup')
            response_content = self.client.get(url).content.decode('utf-8')
            self.assertIn('Registros de novas contas temporariamente suspenso.', response_content)

        except urls.NoReverseMatch as e:
            raise unittest.SkipTest('URL de registro não está ativada.') from e


class DisableSignupAdapterTestAPI(APITestCase):
    """Verifica a suspensão de registro no site via api."""

    @override_settings(
        ACCOUNT_ADAPTER='core.adapters.DisableSignupAdapter',
        REST_AUTH_REGISTER_SERIALIZERS={
            'REGISTER_SERIALIZER': 'core.serializers.DisableSignupSerializer'
        }
    )
    def test_disable_signup_api(self):
        """Verifica se o processo de registro no site é suspenso via api."""
        try:
            url = urlresolvers.reverse('rest_register')
            data = dict(username='u', email='e@b.com', password1='secret123', password2='secret123')
            response = self.client.post(url, data)
            self.assertEqual(
                response.data['non_field_errors'][0],
                'Registro de novas contas temporariamente suspenso.'
            )

        except urls.NoReverseMatch as e:
            raise unittest.SkipTest('URL de registro não está ativada.') from e
