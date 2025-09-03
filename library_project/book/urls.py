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
    )
]
