from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from shop.consumers import YourConsumer
from django.urls import path

websocket_urlpatterns = [path('ws/some_path/', YourConsumer.as_asgi())]
