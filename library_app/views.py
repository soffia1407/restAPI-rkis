from django.shortcuts import render, redirect, get_object_or_404 # Импорт функций для работы с редиректами, шаблонами и 404
from .models import Book, Author # Импорт наших моделей
from .forms import BookForm # Импорт нашей формы
from django.db.models import Q # Импорт Q для сложных запросов

def index(request):
    """Главная страница со списком книг."""
    books = Book.objects.all() # Получаем все книги
    return render(request, 'library_app/index.html', {'books': books}) # Рендерим шаблон и передаем данные

def add_book(request):
    """Страница добавления книги."""
    if request.method == 'POST': # Если форма отправлена
        form = BookForm(request.POST) # Создаем форму с данными
        if form.is_valid(): # Проверяем валидность
            # Получаем данные из формы
            title = form.cleaned_data['title']
            author_name = form.cleaned_data['author_name']
            year = form.cleaned_data['year']
            genre = form.cleaned_data['genre']
            category = form.cleaned_data['category']
            publisher = form.cleaned_data['publisher']
            cover_image = form.cleaned_data['cover_image']
            text_file = form.cleaned_data['text_file']

            author, created = Author.objects.get_or_create(name=author_name) # Получаем или создаем автора
            book = Book(title=title, author=author, year=year, genre=genre, category=category, publisher=publisher,
                        cover_image=cover_image, text_file=text_file) # Создаем книгу

            try:
                book.full_clean() # Проверяем на валидность
                book.save() # Сохраняем книгу
            except Exception as e:
                form.add_error(None, f"Ошибка: {e}") # Ловим ошибку если есть
                return render(request, 'library_app/add_book.html', {'form': form}) # Если ошибка, то заново показываем форму

            return redirect('index') # Перенаправляем на главную
    else:
        form = BookForm() # Создаем пустую форму
    return render(request, 'library_app/add_book.html', {'form': form}) # Показываем форму

def book_detail(request, book_id):
    """Страница с информацией о книге."""
    book = get_object_or_404(Book, pk=book_id) # Получаем книгу по id, 404 если нет
    return render(request, 'library_app/book_detail.html', {'book': book}) # Рендерим шаблон и передаем книгу

def authors(request):
    """Страница со списком авторов."""
    authors = Author.objects.all() # Получаем всех авторов
    return render(request, 'library_app/authors.html', {'authors': authors}) # Рендерим шаблон

def author_detail(request, author_id):
    """Страница с информацией об авторе."""
    author = get_object_or_404(Author, pk=author_id) # Получаем автора, 404 если нет
    return render(request, 'library_app/author_detail.html', {'author': author}) # Рендерим шаблон

def search(request):
    """Страница поиска."""
    query = request.GET.get('query', '').lower() # Получаем поисковый запрос
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) | # Поиск по названию
            Q(genre__icontains=query) | # Поиск по жанру
            Q(author__name__icontains=query) # Поиск по имени автора
        ) # Фильтруем книги по запросу
    else:
        books = [] # Если ничего нет
    return render(request, 'library_app/search.html', {'books': books, 'query': query}) # Рендерим шаблон с результатами