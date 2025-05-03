from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from logs.consumers import LogConsumer  # exemple, à adapter à ton app

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/logs/", LogConsumer.as_asgi()),
        ])
    ),
})
