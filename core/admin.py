from django.contrib import admin

from core.models import Task, Tag

admin.site.register(Task)
admin.site.register(Tag)
