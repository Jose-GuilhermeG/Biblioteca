#imports
from django.urls import path,re_path

#views
from . import views

#urls
urlpatterns = [
    path(
        'list/',
        views.BookListView.as_view(),
        name='book_list'
    ),
    path(
        'create/',
        views.BookCreateView.as_view(),
        name='book_create'
    ),
    path(
        'detail/<str:slug>/',
        views.BookDetailView.as_view(),
        name='book_detail'
    ),
    path(
        'search/<str:title>/',
        views.BookSearchView.as_view(),
        name='book_search'
    ),
    path(
        'category/list/',
        views.CategoryListView.as_view(),
        name='category_list',
    ),
    path(
        'category/create/',
        views.CategoryCreateView.as_view(),
        name='category_create',
    ),
    path(
        'category/detail/<str:slug>/',
        views.CategoryDetailView.as_view(),
        name='category_detail'
    )
]
