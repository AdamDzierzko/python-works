from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Tasks to do in admin panel"""
    search_fields = ['opis']
    list_display = ('id', 'opis')
