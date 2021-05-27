from django.urls import path
from .views import SendMessage, ChatPage


urlpatterns = [
    path('message/', SendMessage.as_view()),
    path('', ChatPage.as_view()),
]
