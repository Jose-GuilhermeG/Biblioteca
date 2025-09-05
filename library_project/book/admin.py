#imports
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

#models
from .models import Book,Category

#models admin

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','created_at']
    search_fields = ['title','description']
    search_help_text = _("Pesquisar por titulo ou descrição")
    prepopulated_fields = {"slug" : ['title']}
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','created_at']
    search_fields = ['title']
    search_help_text = _("Pesquisar categoria pelo nome")
    prepopulated_fields = {"slug" : ['name']}


# Register your models here.