"""Módulo de configuração de urls do projeto."""

from django.conf import settings, urls
from django.conf.urls import static
from django.contrib import admin

from . import views

urlpatterns = [
    urls.url(r'^$', views.redirect_index_view),
    urls.url(r'^home/$', views.index_view, name='home'),
    urls.url(r'^sobre/$', views.sobre_view, name='sobre'),
    urls.url(r'^profissionais/', urls.include('profissionais.urls', namespace='profissionais')),
    urls.url(r'^contato/', urls.include('contato.urls', namespace='contato')),
    # urls.url(r'^rest_auth/', urls.include('rest_auth.urls')),
    # urls.url(r'^rest_auth/registration/', urls.include('rest_auth.registration.urls')),
    # urls.url(r'^contas/', urls.include('allauth.urls')),
    # urls.url(r'^api-auth/', urls.include('rest_framework.urls', namespace='rest_framework')),
    urls.url(r'^admin/', urls.include(admin.site.urls)),
]

# media files in development
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [urls.url(r'^__debug__/', urls.include(debug_toolbar.urls))]
