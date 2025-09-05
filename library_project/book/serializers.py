#imports
from rest_framework import serializers
from django.utils.text import slugify

#models
from .models import Book,Category

#serializers
class CategorySerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Category
        exclude = ['created_by','created_at','updated_at','updated_by','id','slug']
        
    def save(self, **kwargs):
        self.validated_data['slug'] = slugify(self.validated_data.get("name"))
        return super().save(**kwargs)
        
class BookSerializer(
    serializers.ModelSerializer
):
    author_name = serializers.CharField(source='author',read_only=True)
    
    category = CategorySerializer(many=True,required=False)
        
    class Meta:
        model = Book
        exclude = ['created_by','created_at','updated_at','updated_by','id','slug']
        extra_kwargs = {"author" : {"write_only" : True}}
        
    def save(self, **kwargs):
        self.validated_data['slug'] = slugify(self.validated_data.get("title"))
        return super().save(**kwargs)
    