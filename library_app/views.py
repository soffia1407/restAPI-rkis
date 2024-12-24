from django.shortcuts import render, redirect, get_object_or_404 # Функции для работы с редиректами, шаблонами и 404
from .models import Book, Author # Импорт наших моделей
from django.db.models import Q  # Импорт Q для сложных запросов
from rest_framework import viewsets
from .serializers import BookSerializer, AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer  # Связь с сериализатором

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer # Связь с сериализатором

def index(request):
    """Главная страница со списком книг."""
    books = Book.objects.all() # Получаем все книги
    return render(request, 'library_app/index.html', {'books': books}) # Рендерим шаблон

def book_detail(request, book_id):
    """Страница с информацией о книге."""
    book = get_object_or_404(Book, pk=book_id) # Получаем книгу по ID или 404
    return render(request, 'library_app/book_detail.html', {'book': book}) # Отображаем информацию о книге

def authors(request):
    """Страница со списком авторов."""
    authors = Author.objects.all() # Получаем всех авторов
    return render(request, 'library_app/authors.html', {'authors': authors}) # Отображаем список авторов

def author_detail(request, author_id):
    """Страница с информацией об авторе."""
    author = get_object_or_404(Author, pk=author_id) # Получаем автора по ID или 404
    return render(request, 'library_app/author_detail.html', {'author': author}) # Отображаем информацию об авторе

def search(request):
    """Страница поиска книг."""
    query = request.GET.get('query', '').lower() # Получаем поисковый запрос, переводим в нижний регистр
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) |
            Q(genre__icontains=query) |
            Q(author__name__icontains=query)
        ) # Фильтруем книги по запросу
    else:
        books = []  # Если нет запроса, то ничего не ищем
    return render(request, 'library_app/search.html', {'books': books, 'query': query}) # Отображаем результаты поиска