#imports
import django_filters as filters

#models
from .models import Book

#filtros
class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr="icontains")
    
    class Meta:
        model = Book
        fields = ['author']
        
