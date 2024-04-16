from django.test import TestCase
from library_app.models import Book, Genre, Author


def create_model_tests(model_class, creation_attrs):
    class ModelTest(TestCase):
        def test_successful_creation(self):
            model_class.objects.create(**creation_attrs)
    return ModelTest

BookModelTest = create_model_tests(Book,  {'title': 'ABC', 'volume': 123})
GenreModelTest = create_model_tests(Genre, {'name': 'ABC'})
AuthorModelTest = create_model_tests(Author, {'full_name': 'ABC'})
