from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Author, Genre, Book, BookGenre, BookAuthor
from datetime import date
from django.utils.translation import gettext_lazy as _

class RecencyBookFilter(admin.SimpleListFilter):
    title = _('recency')
    parameter_name = 'recency'
    _ten_yo = '10yo'
    _twenty_yo = '20yo'

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[str, str]]:
        return (
            (self._ten_yo, _('Created in the last 10 years')),
            (self._twenty_yo, _('Created in the last 20 years')),
        )
    
    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        decade = 10
        year_today = date.today().year
        if self.value() == self._ten_yo:
            return queryset.filter(year__gte=year_today-decade)
        elif self.value() == self._twenty_yo:
            return queryset.filter(year__gte=year_today-decade*2)
        return queryset

class BookAuthorInline(admin.TabularInline):
    model = BookAuthor
    extra = 1
    
class BookGenreInline(admin.TabularInline):
    model = BookGenre
    extra = 1

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    model = Author
    inlines = (BookAuthorInline,)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    model = Genre

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    model = Book
    inlines = (BookAuthorInline, BookGenreInline)
    list_filter = (
        'type',
        'genres',
        RecencyBookFilter,
    )

@admin.register(BookGenre)
class BookGenreAdmin(admin.ModelAdmin):
    model = BookGenre

@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    model = BookAuthor