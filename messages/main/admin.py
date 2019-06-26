from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'email', 'sent_to', 'user')
    list_display_links = ['text']


admin.site.register(Message, MessageAdmin)

