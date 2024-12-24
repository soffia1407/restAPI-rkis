"""
URL configuration for library_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers # Очень важный импорт
from library_app import views

router = routers.DefaultRouter()  # Создаем роутер
router.register('books', views.BookViewSet)  # Регистрируем BookViewSet
router.register('authors', views.AuthorViewSet)  # Регистрируем AuthorViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library_app.urls')),
    path('api/', include(router.urls))  # Маршруты для REST API
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)