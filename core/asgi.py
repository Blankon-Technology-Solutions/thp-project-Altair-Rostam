import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from todo.routing import wsPattern

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

http_response_app = get_asgi_application()
application = ProtocolTypeRouter({"http": http_response_app, "websocket": URLRouter(wsPattern)})
