from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Author(models.Model):
    """Модель автора книги."""
    name = models.CharField(max_length=100, unique=True)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    """Модель книги."""
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(9999)])  # Год выпуска с валидацией
    genre = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True) # Обложка
    text_file = models.FileField(upload_to='texts/', blank=True, null=True)  # Файл с текстом

    class Meta:
        unique_together = ('title', 'author', 'year', 'publisher')

    def __str__(self):
        return self.title