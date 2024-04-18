from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator

from .models import Book, Genre, Author, Client
from .forms import TestForm, Registration

def home_page(request):
    return render(
        request,
        'index.html',
        {
            'books': Book.objects.count(),
            'genres': Genre.objects.count(),
            'authors': Author.objects.count(),
        }
    )

def create_list_view(model_class, plural_name, template):
    class CustomListView(ListView):
        model = model_class
        template_name = template
        paginate_by = 10
        context_object_name = plural_name

        def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
            context = super().get_context_data(**kwargs)
            books = model_class.objects.all()
            paginator = Paginator(books, 10)
            page = self.request.GET.get('page')
            page_obj = paginator.get_page(page)
            context[f'{plural_name}_list'] = page_obj
            return context
    return CustomListView

BookListView = create_list_view(Book, 'books', 'catalog/books.html')
AuthorListView = create_list_view(Author, 'authors', 'catalog/authors.html')
GenreListView = create_list_view(Genre, 'genres', 'catalog/genres.html')

def create_view(model_class, context_name, template):
    def view(request):
        id_ = request.GET.get('id', None)
        target = model_class.objects.get(id=id_) if id_ else None
        return render(
            request,
            template,
            {
                context_name: target,
            }
        )
    return view

book_view = create_view(Book, 'book', 'entities/book.html')
genre_view = create_view(Genre, 'genre', 'entities/genre.html')
author_view = create_view(Author, 'author', 'entities/author.html')

def test_form(request):
    context = {'form': TestForm()}
    for key in ('text', 'number', 'choice'):
        context[key] = request.GET.get(key, f'{key} is not provided')
    return render(
        request,
        'pages/test_form.html',
        context,
    )

def register(request):
    errors = ''
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            user = form.save()
            Client.objects.create(user=user)
        else:
            errors = form.errors
    else:
        form = Registration()

    return render(
        request,
        'registration/register.html',
        {
            'form': form,
            'errors': errors,
        }
    )