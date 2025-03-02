from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('news/', views.news_list, name='news_list'),  # Список новостей
    path('news/<int:post_id>/', views.news_detail, name='news_detail'),  # Детальная страница новости
]