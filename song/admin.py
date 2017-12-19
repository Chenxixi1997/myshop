from django.contrib import admin
from .models import Songlist, Song

class SonglistAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name', )}
admin.site.register(Songlist, SonglistAdmin)

class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'count', 'available', 'created', 'updated')
    list_filter = ('available', 'created', 'updated')
    list_editable = ('count', 'available')
    prepopulated_fields = {'slug': ('name', )}
admin.site.register(Song, SongAdmin)