# import time
from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


from .helpers import get_rasa_message, clean_text, get_language_bnl
from . import config
from .models import ChatHistory
from .suggestion_helper import auto_complete


class ChatPage(View):

    def get(self, request, format=None):
        return render(request, 'homepage.html', {}, 200)


class SendMessage(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        try:
            sender = request.data.get('sender', 'user')
            raw_message = request.data.get('message', '')
            message = clean_text(raw_message)
            # print(message)
            if len(message) < 2:
                return Response({"text": config.ERR_TXT}, status=200)

            rasa_text = get_rasa_message(sender, message)
            new_chat = ChatHistory.objects.create(
                input_text=raw_message,
                reply_text=rasa_text
            )
            new_chat.save()

            return Response({"text": rasa_text}, status=200)
        except Exception as e:
            print(str(e))
            return Response({"text": config.ERR_TXT}, status=200)


class GetSuggestions(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        try:
            chat_text = request.data.get('chat_text')
            lang = get_language_bnl(chat_text)

            resp = {
                "suggestions": auto_complete(chat_text, lang)
            }
            return Response(resp, status=200)
        except Exception as e:
            print(str(e))
            return Response({"text": config.ERR_TXT}, status=200)

