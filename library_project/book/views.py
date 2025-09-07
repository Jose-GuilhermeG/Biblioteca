#imports
from rest_framework import generics
from rest_framework import permissions
from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _
from django.db.models.functions import Lower
from .filters import BookFilter

from .permissions import CretaedByUserOrReadOnly

from core.mixins import SuccessFullCreateMessageMixin,SuccessFullUpdatedMessageMixin

#serializer
from .serializers import BookSerializer,CategorySerializer,BookListSerializer

#model
from .models import Book,Category

# Create your views here.
class BookListView(
    generics.ListAPIView
):
    queryset = Book.objects.all().order_by(Lower("title"))
    serializer_class = BookListSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = BookFilter
    
class BookCreateView(
    SuccessFullCreateMessageMixin,
    generics.CreateAPIView,
):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    message = _('Created sucefully')
    
    def perform_create(self, serializer):
        request = self.request
        serializer.save(
            created_by = request.user,
            updated_by = request.user
        )
        
    
class BookDetailView(
    SuccessFullUpdatedMessageMixin,
    generics.RetrieveUpdateDestroyAPIView,
):
    permission_classes = [CretaedByUserOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'
    
    def perform_update(self, serializer):
        serializer.save(
            updated_by = self.request.user
        )
    
class BookSearchView(
    generics.ListAPIView
):
    serializer_class = BookListSerializer
    
    def get_queryset(self):
        kwargs:dict = self.kwargs
        title:str = kwargs.get("title")
        queryset = Book.objects.filter(title__icontains = title).order_by(Lower("title"))
        return queryset
    
class CategoryListView(
    generics.ListAPIView
):
    queryset = Category.objects.all().order_by(Lower("name"))
    serializer_class = CategorySerializer
    
class CategoryCreateView(
    SuccessFullCreateMessageMixin,
    generics.CreateAPIView
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    message = _('Created sucefully')
    
    def perform_create(self, serializer):
        request = self.request
        serializer.save(
            created_by = request.user,
            updated_by = request.user
        )
        
        
class CategoryDetailView(
    SuccessFullUpdatedMessageMixin,
    generics.RetrieveUpdateDestroyAPIView
):
    permission_classes = [CretaedByUserOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    
     
    def perform_update(self, serializer):
        serializer.save(
            updated_by = self.request.user
        )