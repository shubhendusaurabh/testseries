from django.contrib import admin

from .models import *

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'chapter', 'created_at',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Unit)
admin.site.register(Chapter)
admin.site.register(Exam)
admin.site.register(Subject)
