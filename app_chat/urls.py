from django.urls import path
from app_chat.views import chat_views

urlpatterns = [
    path('chat/', chat_views),
]
