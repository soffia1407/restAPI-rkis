from django.shortcuts import render, redirect, get_object_or_404 # Функции для работы с редиректами, шаблонами и 404
from .models import Book, Author # Импорт наших моделей
from .forms import BookForm  # Импорт нашей формы
from django.db.models import Q  # Импорт Q для сложных запросов
from django.conf import settings  # Для работы с настройками проекта
from django.core.files.storage import FileSystemStorage # Для работы с файловой системой

def index(request):
    """Главная страница со списком книг."""
    books = Book.objects.all() # Получаем все книги
    return render(request, 'library_app/index.html', {'books': books}) # Рендерим шаблон

def add_book(request):
    """Страница добавления книги."""
    if request.method == 'POST': # Если форма отправлена методом POST
        form = BookForm(request.POST, request.FILES)  # Создаем форму, передаем данные формы и файлы
        if form.is_valid():  # Проверяем валидность формы
            # Получаем данные из формы (текстовые поля)
            title = form.cleaned_data['title']
            author_name = form.cleaned_data['author_name']
            year = form.cleaned_data['year']
            genre = form.cleaned_data['genre']
            category = form.cleaned_data['category']
            publisher = form.cleaned_data['publisher']
            cover_image = request.FILES.get('cover_image')  # Получаем файл обложки из request.FILES
            text_file = request.FILES.get('text_file') # Получаем файл с текстом из request.FILES

            author, created = Author.objects.get_or_create(name=author_name)  # Получаем или создаем автора
            book = Book(title=title, author=author, year=year, genre=genre, category=category, publisher=publisher,
                        cover_image=cover_image, text_file=text_file) # Создаем книгу

            try:
                book.full_clean() # Выполняем полную валидацию модели
                book.save()
            except Exception as e: # Если есть ошибка при сохранении
                form.add_error(None, f"Ошибка при добавлении книги: {e}") # Добавляем ошибку в форму
                return render(request, 'library_app/add_book.html', {'form': form}) # Возвращаем форму с ошибкой

            return redirect('index')  # Перенаправляем на главную страницу
    else:
        form = BookForm()  # Если GET, создаем пустую форму
    return render(request, 'library_app/add_book.html', {'form': form}) # Отображаем форму

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
            Q(title__icontains=query) |  # Поиск по названию
            Q(genre__icontains=query) |  # Поиск по жанру
            Q(author__name__icontains=query)  # Поиск по имени автора
        ) # Фильтруем книги по запросу
    else:
        books = []  # Если нет запроса, то ничего не ищем
    return render(request, 'library_app/search.html', {'books': books, 'query': query}) # Отображаем результаты поиска