from django.contrib import admin

from .models import *

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Unit)
admin.site.register(Chapter)
admin.site.register(Exam)
admin.site.register(Subject)
