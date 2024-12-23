from django.db import models

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
    year = models.IntegerField()
    genre = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    cover_image = models.CharField(max_length=200)
    text_file = models.CharField(max_length=200)

    class Meta:
        unique_together = ('title', 'author', 'year', 'publisher') # Уникальность

    def __str__(self):
        return self.title