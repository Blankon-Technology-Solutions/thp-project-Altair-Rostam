import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from todo.routing import wsPattern

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = ProtocolTypeRouter(
    {"http": get_asgi_application(), "websocket": URLRouter(wsPattern)}
)
