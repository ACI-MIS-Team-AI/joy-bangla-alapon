from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Intent(models.Model):
    name = models.CharField(max_length=32, blank=False, unique=True)
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='creator_intent',
        null=True, blank=True
    )
    ts_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class SubIntent(models.Model):
    name = models.CharField(max_length=32, blank=True)
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='creator_sub_intent',
        null=True, blank=True
    )
    ts_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Response(models.Model):
    text_en = models.TextField(blank=True)
    text_bn = models.TextField(blank=True)
    intent = models.ForeignKey(
        Intent,
        on_delete=models.SET_NULL,
        related_name='response_intent',
        null=True, blank=False
    )
    sub_intent = models.ForeignKey(
        SubIntent,
        on_delete=models.SET_NULL,
        related_name='response_sub_intent',
        null=True, blank=True
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='creator_response',
        null=True, blank=True
    )
    ts_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text_en


class Question(models.Model):
    text_en = models.TextField(blank=True)
    text_bn = models.TextField(blank=True)
    text_bnl = models.TextField(blank=True)
    intent = models.ForeignKey(
        Intent,
        on_delete=models.SET_NULL,
        related_name='question_intent',
        null=True, blank=False
    )
    sub_intent = models.ForeignKey(
        SubIntent,
        on_delete=models.SET_NULL,
        related_name='question_sub_intent',
        null=True, blank=True
    )
    response = models.ForeignKey(
        Response,
        on_delete=models.SET_NULL,
        related_name='question_response',
        null=True, blank=False
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='creator_question',
        null=True, blank=True
    )
    ts_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text_en
