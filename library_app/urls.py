from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_book/', views.add_book, name='add_book'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('authors/', views.authors, name='authors'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('search/', views.search, name='search'),

]