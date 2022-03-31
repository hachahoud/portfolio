from django.contrib import admin

from .models import Film, Entry, Message

admin.site.register(Film)
admin.site.register(Entry)
admin.site.register(Message)
