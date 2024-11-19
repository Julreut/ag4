from django.urls import path
from .views import get_newspapers, article_list, detailed_article

app_name ='articles'

urlpatterns = [
    path('', get_newspapers, name='news-papers'),
    path('article_list/', article_list, name='all-articles'),
    path('<slug:slug>/', detailed_article, name='detailed-article'),
]