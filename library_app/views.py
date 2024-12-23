from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Author
from .forms import BookForm
from django.db.models import Q


def index(request):
    books = Book.objects.all()
    return render(request, 'library_app/index.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author_name = form.cleaned_data['author_name']
            year = form.cleaned_data['year']
            genre = form.cleaned_data['genre']
            category = form.cleaned_data['category']
            publisher = form.cleaned_data['publisher']
            cover_image = form.cleaned_data['cover_image']
            text_file = form.cleaned_data['text_file']

            author, created = Author.objects.get_or_create(name=author_name)

            book = Book(title=title, author=author, year=year, genre=genre, category=category, publisher=publisher,
                        cover_image=cover_image, text_file=text_file)

            try:
                book.full_clean()
                book.save()
            except Exception as e:
                form.add_error(None, f"Ошибка при добавлении книги: {e}")
                return render(request, 'library_app/add_book.html', {'form': form})

            return redirect('index')
    else:
        form = BookForm()
    return render(request, 'library_app/add_book.html', {'form': form})


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'library_app/book_detail.html', {'book': book})


def authors(request):
    authors = Author.objects.all()
    return render(request, 'library_app/authors.html', {'authors': authors})


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'library_app/author_detail.html', {'author': author})


def search(request):
    query = request.GET.get('query', '').lower()
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) |
            Q(genre__icontains=query) |
            Q(author__name__icontains=query)
        )
    else:
        books = []
    return render(request, 'library_app/search.html', {'books': books, 'query': query})