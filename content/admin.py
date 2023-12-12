from django.contrib import admin
from .models import Content

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['listing','contact','image']
    list_filter = ['contact']
    ordering = ['contact']

