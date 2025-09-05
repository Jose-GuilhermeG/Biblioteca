#imports
from rest_framework import generics
from rest_framework import permissions
from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _
from django.db.models.functions import Lower
from .filters import BookFilter

from core.mixins import SuccessFullCreateMessageMixin

#serializer
from .serializers import BookSerializer,CategorySerializer

#model
from .models import Book,Category

# Create your views here.
class BookListView(
    generics.ListAPIView
):
    queryset = Book.objects.all().order_by(Lower("title"))
    serializer_class = BookSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = BookFilter
    
class BookCreateView(
    SuccessFullCreateMessageMixin,
    generics.CreateAPIView
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
    generics.RetrieveUpdateDestroyAPIView
):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'
    
    def perform_update(self, serializer):
        serializer.save(
            updated_by = self.request.user
        )
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response['message'] = 'Updated sucefully'
        return response
    
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
    generics.RetrieveUpdateDestroyAPIView
):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    
     
    def perform_update(self, serializer):
        serializer.save(
            updated_by = self.request.user
        )
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response['message'] = 'Updated sucefully'
        return response