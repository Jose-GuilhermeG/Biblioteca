#imports
import django_filters as filters

#models
from .models import Book,Category

#filtros
class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr="icontains")
    
    author = filters.CharFilter(
        field_name="author__username",
        lookup_expr="icontains",
        label="Nome do author"
    )
    
    category= filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        field_name='category__name',
        label = 'Categorias do livro'
    )
    
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
        fields = []
        
