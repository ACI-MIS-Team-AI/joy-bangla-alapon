from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class ChatHistory(models.Model):
    input_text = models.TextField(blank=True)
    reply_text = models.TextField(blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
