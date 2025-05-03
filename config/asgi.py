import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import logs.routing  # ou ton fichier qui contient les routes WS

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # requêtes HTTP classiques
    "websocket": AuthMiddlewareStack(
        URLRouter(
            logs.routing.websocket_urlpatterns,
            #accounts.routing.websocket_urlpatterns  # ou 
        )
    ),
})
