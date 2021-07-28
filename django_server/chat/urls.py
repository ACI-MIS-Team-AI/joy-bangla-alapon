from django.urls import path
from . import views


urlpatterns = [
    path('message/', views.SendMessage.as_view()),
    path('suggestion/', views.GetSuggestions.as_view()),
    path('', views.ChatPage.as_view()),
]
