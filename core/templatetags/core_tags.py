"""Este módulo contem tags e filtros globais em relação ao projeto."""

import hashlib

from django import template

register = template.Library()


@register.simple_tag
def gravatar_url(email):
    """Obtém a url gravatar em função do email fornecido."""
    return '//www.gravatar.com/avatar/{}'.format(hashlib.md5(email.encode('utf-8')).hexdigest())


@register.simple_tag(takes_context=True)
def active_link(context, trecho_url, classe_ativa='nav-active'):
    """Obtém uma classe ativa caso a url do recurso atual contenha trecho_url."""
    return classe_ativa if trecho_url in context['request'].path else ''
