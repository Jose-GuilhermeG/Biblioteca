#imports
from rest_framework import serializers
from django.utils.text import slugify

#models
from .models import Book

#serializers
class BookSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Book
        exclude = ['created_by','created_at','updated_at','updated_by','id','slug']
        
    def save(self, **kwargs):
        self.validated_data['slug'] = slugify(self.validated_data.get("title"))
        return super().save(**kwargs)