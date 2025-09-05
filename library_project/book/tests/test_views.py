#imports
from rest_framework.test import APITestCase
from model_bakery import baker
from django.urls import reverse
from json import loads

#models
from book.models import Book
from django.contrib.auth import get_user_model

USER = get_user_model()

#serializers
from book.serializers import BookSerializer

#tests
class BasicBookViewsTests(APITestCase):
    """simple tests"""
    
    def setUp(self):
        self.author = baker.make(USER)
        self.loged_client = self.loged_cliente_by_author()
        
    def tearDown(self):
        Book.objects.all().delete()
                
    def loged_cliente_by_author(self):
        loged_client = self.client
        loged_client.force_login(user=self.author)
        return loged_client
            
    def test_book_created_view(self):
        url = reverse("book:book_create")
        book_object = baker.prepare(Book,author=self.author,content='')
        serializer = BookSerializer(book_object)
        data = serializer.data
        data['file'] = ""
        response = self.loged_client.post(url,data)
        
        self.assertEqual(response.status_code,201,response.content)
        self.assertEqual(Book.objects.all().count(),1)

    def test_book_list_view(self):
        books = baker.make(Book,author=self.author, _quantity=5)
        url = reverse("book:book_list")
        response = self.client.get(url)
        serializer = BookSerializer(books,many=True)
        
        for obj in response.json():
            if not obj in serializer.data:
                assert False , "Objeto não cadastrado mas amostra"
        
        self.assertIsNotNone(response.json())
        self.assertEqual(response.status_code,200)
        
    