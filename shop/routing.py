from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import re_path, path
from .consumers import ChatConsumer


websocket_urlpatterns = [path("ws/chat/lobby/<str:session_uuid>/", ChatConsumer.as_asgi()),]

