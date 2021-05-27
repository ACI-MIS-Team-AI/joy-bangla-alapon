from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from .models import Intent, SubIntent, Response, Question


class QuestionInline(admin.TabularInline):
    model = Question

    fields = [
        'text_en', 'text_bn', 'text_bnl'
    ]

    formfield_overrides = {
        # models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 40})},
    }

    def get_extra(self, request, obj=None, **kwargs):
        extra = 0
        # return extra - obj.field.count()
        return extra


class ResponseAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline
    ]

    search_fields = ('text_en', 'text_bn')
    list_filter = (
        'intent', 'sub_intent'
    )

    list_display = (
        'text_en',
        'text_bn',
        'intent',
        'question_list_bnl',
        'question_list_bn'
    )

    def question_list_bnl(self, obj):
        qts = Question.objects.filter(
            response_id=obj.id
        )
        qts_list = [qt.text_bnl for qt in qts]
        resp = "+".join(qts_list)
        return resp

    def question_list_bn(self, obj):
        qts = Question.objects.filter(
            response_id=obj.id
        )
        qts_list = [qt.text_bn for qt in qts]
        resp = "+".join(qts_list)
        return resp


class QuestionAdmin(admin.ModelAdmin):

    search_fields = ('text_en', 'text_bn', 'text_bnl')
    list_filter = (
        'intent', 'sub_intent'
    )

    list_display = (
        'text_en',
        'text_bn',
        'text_bnl',
        'intent',
        'sub_intent'
    )


class IntentAdmin(admin.ModelAdmin):

    search_fields = ('name',)

    list_display = (
        'name',
        'creator'
    )


class SubIntentAdmin(admin.ModelAdmin):

    search_fields = ('name',)

    list_display = (
        'name',
        'creator'
    )


admin.site.register(Response, ResponseAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Intent, IntentAdmin)
admin.site.register(SubIntent, SubIntentAdmin)
