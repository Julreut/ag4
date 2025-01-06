"""
ASGI config for fakebook project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application



# from fakebook import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fakebook.settings')
application = get_asgi_application()

