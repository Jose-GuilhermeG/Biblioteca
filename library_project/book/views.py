#imports
from rest_framework import generics
from rest_framework import permissions
from django_filters import rest_framework as filters
from django.db.models.functions import Lower
from .filters import BookFilter

#serializer
from .serializers import BookSerializer

#model
from .models import Book

# Create your views here.
class BookListView(
    generics.ListAPIView
):
    queryset = Book.objects.all().order_by(Lower("title"))
    serializer_class = BookSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = BookFilter
    
class BookCreateView(
    generics.CreateAPIView
):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def perform_create(self, serializer):
        request = self.request
        serializer.save(
            created_by = request.user,
            updated_by = request.user
        )
        
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response['message'] = 'Created sucefully'
        return response
    
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