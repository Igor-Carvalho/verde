"""Testa views da aplicação profissionais."""

from django import test
from django.core import urlresolvers


class ProfissionaisViewTest(test.SimpleTestCase):
    """Testa a view de profissionais."""

    def test_get_templates_profissional(self):
        """Testa o carregamento de templates para um dado profissional."""
        response = self.client.get(urlresolvers.reverse('profissionais:profissional', args=['andré_luiz']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual([t.name for t in response.templates][0], 'profissionais/andré_luiz.html')
