#imports
import django_filters as filters

#models
from .models import Book

#filtros
class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr="icontains")
    
    max_price = filters.NumberFilter(
        field_name='price',
        lookup_expr='lt'
    )
    
    min_price = filters.NumberFilter(
        field_name='price',
        lookup_expr='gt'
    )
    
    class Meta:
        model = Book
        fields = ['author']
        
