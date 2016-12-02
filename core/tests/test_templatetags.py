"""Testes relacionados a tags e filtros da aplicação core."""

import hashlib
import unittest

from django import template
from django.test import client

from ..templatetags import core_tags


class CoreSimpleTagsTests(unittest.TestCase):
    """Testes de tags simples."""

    def test_gravatar_url(self):
        """Verifica se a url gravatar é gerada corretamente em função do email fornecido."""
        email = 'admin@domain.com'
        hash_email = hashlib.md5(email.encode('utf-8')).hexdigest()

        url = core_tags.gravatar_url(email)
        self.assertEqual(url, '//www.gravatar.com/avatar/{}'.format(hash_email))

    def test_active_link(self):
        """Verifica se a classe para um link ativo é gerada corretamente."""
        get_request = client.RequestFactory().get('/home/')
        content = template.Template(
            '{% load active_link from core_tags %}'
            '{% active_link "home" %}'
        ).render(template.Context(dict(request=get_request)))
        self.assertEqual(content, 'nav-active')

        get_request = client.RequestFactory().get('/serviços/porcelanato/')
        content = template.Template(
            '{% load active_link from core_tags %}'
            '{% active_link "serviços" %}'
        ).render(template.Context(dict(request=get_request)))
        self.assertEqual(content, 'nav-active')
