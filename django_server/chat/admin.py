from django.contrib import admin
from .models import ChatHistory


class ChatHistoryAdmin(admin.ModelAdmin):
    search_fields = ('input_text', 'reply_text', )

    list_filter = (
        'timestamp',
    )

    list_display = (
        'timestamp',
        'input_text',
        'reply_text',
    )


admin.site.register(ChatHistory, ChatHistoryAdmin)
