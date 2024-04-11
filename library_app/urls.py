from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='homepage'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/', views.book_view, name='book'),
]