from django import forms
from .models import Author, Book


class BookForm(forms.ModelForm):
    author_name = forms.CharField(max_length=100, required=True, label='Автор')
    class Meta:
        model = Book
        fields = ['title', 'year', 'genre', 'category', 'publisher', 'cover_image', 'text_file']
        labels = {
            'title': 'Название',
             'year': 'Год',
             'genre': 'Жанр',
             'category': 'Категория',
             'publisher': 'Издательство',
             'cover_image': 'Ссылка на обложку',
              'text_file': 'Ссылка на файл',
        }