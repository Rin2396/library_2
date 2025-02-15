from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home_page, name='homepage'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/', views.book_view, name='book'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/', views.author_view, name='author'),
    path('genres/', views.GenreListView.as_view(), name='genres'),
    path('genre/', views.genre_view, name='genre'),
    path('test_form/', views.test_form, name='test_form'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]