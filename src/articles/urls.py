from django.urls import path
from .views import get_newspapers, get_articles, detailed_article

app_name ='articles'

urlpatterns = [
    path('', get_newspapers, name='news-paper'),
    path('all_articles', get_articles, name='all-articles'),
    path('<slug>/', detailed_article, name='detailed-article'),
]