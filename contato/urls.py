"""URLs da aplicação contato."""

from django.conf import urls

from . import views

urlpatterns = [
    urls.url(r'^$', views.contato_view, name='contato'),
    urls.url(r'^form/$', views.contato_form_view, name='contato_form_view'),
    urls.url(r'^enviar/formulario/$', views.enviar_formulário_view, name='enviar_formulário'),
]
