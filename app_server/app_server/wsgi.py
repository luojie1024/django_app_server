"""app_server
WSGI config for app_server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_server.settings")

application = get_wsgi_application()
sys.path.append("/var/www/django_app_server/app_server/")
