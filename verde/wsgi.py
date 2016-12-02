"""wsgi module."""

import os

from django.core import wsgi
from whitenoise import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "verde.settings")
application = django.DjangoWhiteNoise(wsgi.get_wsgi_application())
