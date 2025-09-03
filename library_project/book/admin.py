#imports
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

#models
from .models import Book

#models admin

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title','description']
    search_help_text = _("Pesquisar por titulo ou descrição")
    

# Register your models here.
