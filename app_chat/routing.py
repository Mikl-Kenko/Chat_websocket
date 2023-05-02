from django.urls import re_path 
from .consumers import ConsumerChat


websocket_urlpatterns = [
    re_path("" , ConsumerChat.as_asgi()) ,
]
