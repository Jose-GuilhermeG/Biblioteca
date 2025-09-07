#imports
from rest_framework.test import APITestCase
from model_bakery import baker
from django.urls import reverse
from json import loads

from .mixins import ForcedLoggedClient

#models
from book.models import Book,Category
from django.contrib.auth import get_user_model

USER = get_user_model()

#serializers
from book.serializers import BookSerializer

#classes
class BaseBookTestConfig:
    def setUp(self):
        self.author = baker.make(USER)
        self.category = baker.make(Category)
        
    
    def tearDown(self):
        Book.objects.all().delete()
        USER.objects.all().delete()
        Category.objects.all().delete()

#tests
class CreateBookApiViewTest(
    BaseBookTestConfig,
    ForcedLoggedClient,
    APITestCase
):
    def setUp(self):
        super().setUp()
        self.book_data = {'title' : 'test','author' : self.author.id}
        self.url = reverse('book:book_create')
        self.logged_client = self.get_logged_client(self.author)
        
        
    def test_create_book_view_code_and_message(self):
        response = self.logged_client.post(
            self.url,
            self.book_data
        )
        
        self.assertEqual(response.status_code,201)
        self.assertTrue(response.headers.get('message',False))
        
    def test_create_book_view_create_book(self):
        response = self.logged_client.post(self.url,self.book_data)
        books_number = Book.objects.count()
        self.assertEqual(books_number,1)
        
    def test_if_unlogged_user_canot_create_book(self):
        response = self.client.post(self.url,self.book_data)
        books_number = Book.objects.count()
        
        self.assertEqual(response.status_code,403)
        self.assertEqual(books_number,0)
        
    def test_book_created_by_field(self):
        response = self.logged_client.post(self.url,self.book_data)
        book_created_by = Book.objects.get(title=self.book_data.get("title")).created_by
        
        self.assertEqual(self.author,book_created_by)
        
class UpdatedDetailDeleteBookApiViewTest(
    BaseBookTestConfig,
    ForcedLoggedClient,
    APITestCase
):
    def setUp(self):
        super().setUp()
        self.book = baker.make(Book,title='Test',author=self.author,slug='Test',created_by=self.author)
        self.url = reverse("book:book_detail",kwargs={'slug':self.book.slug})
        self.logged_client = self.get_logged_client(self.author)
        
    def test_if_delete_view_works(self):
        response = self.logged_client.delete(self.url)
        books_count = Book.objects.count()
        self.assertEqual(books_count,0)
        
        
class ListBookApiViewTest(
    BaseBookTestConfig,
    APITestCase
):
    def setUp(self):
        super().setUp()
        self.books_quantity = 10
        self.books = baker.make(Book,author=self.author,_quantity=self.books_quantity)
        self.url = reverse("book:book_list")
        
    def test_books_list_quantity(self):
        response = self.client.get(self.url)
        books = response.json()
        books_numeber = len(books)
        self.assertEqual(books_numeber,self.books_quantity)
        
    