"""URLs da aplicação contato."""

from django.conf import urls

from . import views

urlpatterns = [
    urls.url(r'^enviar/formulário/$', views.enviar_formulário_view, name='enviar_formulário'),
]
