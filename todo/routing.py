from django.urls import path

from .consumers import TodoConsumer

wsPattern = [path("ws/todos/", TodoConsumer.as_asgi())]
