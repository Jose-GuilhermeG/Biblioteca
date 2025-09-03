#imports
from rest_framework import serializers

#models
from .models import Book

#serializers
class BookSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Book
        exclude = ['created_by','created_at','updated_at','updated_by','id']
        
    