"""URLs da aplicação profissionais."""

from django.conf import urls

from . import views

urlpatterns = [
    urls.url(r'^(?P<profissional>.+)/$', views.profissional_view, name='profissional'),
]
