"""Views da aplicação profissionais."""

from django.views import generic


class ProfissionalView(generic.TemplateView):
    """Página contendo informações a respeito de um dado profissional."""

    def get_template_names(self):
        """Obtém o template pra um profissional específico."""
        return ['profissionais/{}.html'.format(self.kwargs['profissional'])]


profissional_view = ProfissionalView.as_view()
