# admin.py
from django.contrib import admin
from .models import Archive

class ArchiveEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'content')

admin.site.register(Archive, ArchiveEntryAdmin)
