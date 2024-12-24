from django.contrib import admin
from .models import Author, Book

class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'year', 'genre') # Указываем какие поля будут в списке

admin.site.register(Author)
admin.site.register(Book, BookAdmin)