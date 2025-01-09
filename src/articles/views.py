from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse, get_object_or_404
from .models import Article, NewsPaper
from profiles.models import Profile
from django.db.models import Q

from analytics.models import UserContentPosition

from django.contrib.contenttypes.models import ContentType
import random

# Create your views here.

### Get the newspapers
@login_required
def get_newspapers(request):
    user = request.user
    newspaper_type = ContentType.objects.get_for_model(NewsPaper)

    # Prüfen, ob bereits eine Reihenfolge existiert
    if not UserContentPosition.objects.filter(user=user, content_type=newspaper_type).exists():
        # Randomisiere die Zeitungen
        newspapers = list(NewsPaper.objects.all())
        random.shuffle(newspapers)

        # Speichere die Reihenfolge im UserContentPosition-Modell
        for index, newspaper in enumerate(newspapers):
            UserContentPosition.objects.create(
                user=user,
                content_type=newspaper_type,
                object_id=newspaper.id,
                position=index + 1
            )

    # Lade die gespeicherte Reihenfolge
    newspaper_positions = UserContentPosition.objects.filter(user=user, content_type=newspaper_type).order_by('position')
    newspapers = [pos.content_object for pos in newspaper_positions]

    context = {
        'news_papers': newspapers
    }
    return render(request, 'articles/news_papers.html', context)

## Article definitions
@login_required
def article_list(request, news_paper_id):
    user = request.user
    article_type = ContentType.objects.get_for_model(Article)
    newspaper = get_object_or_404(NewsPaper, id=news_paper_id)

    # IDs aller Artikel der Zeitung abrufen
    article_ids = Article.objects.filter(news_paper_id=news_paper_id).values_list('id', flat=True)

    # Prüfen, ob bereits eine Reihenfolge existiert
    if not UserContentPosition.objects.filter(user=user, content_type=article_type, object_id__in=article_ids).exists():
        # Randomisiere die Artikel für diese Zeitung
        articles = list(Article.objects.filter(news_paper_id=news_paper_id))
        random.shuffle(articles)

        # Speichere die Reihenfolge im UserContentPosition-Modell
        for index, article in enumerate(articles):
            UserContentPosition.objects.create(
                user=user,
                content_type=article_type,
                object_id=article.id,
                position=index + 1
            )

    # Lade die gespeicherte Reihenfolge
    article_positions = UserContentPosition.objects.filter(
        user=user, content_type=article_type, object_id__in=article_ids
    ).order_by('position')
    articles = [pos.content_object for pos in article_positions]

    context = {'articles': articles, 'newspaper': newspaper}
    return render(request, 'articles/all_articles.html', context)


#track article interactions

@login_required
def detailed_article(request, news_paper_id, slug):

    # Hole die Zeitung und prüfe, ob sie existiert
    newspaper = get_object_or_404(NewsPaper, id=news_paper_id)
    # Abrufen des spezifischen Artikels anhand des Slugs
    article = get_object_or_404(Article, slug=slug, news_paper_id=news_paper_id)
    profile = Profile.objects.get(user=request.user)

    public_comments_count = article.comments.filter(
        parent_comment__isnull=True,
    ).filter(
        Q(is_public=True) | Q(author=profile)  # Öffentlich ODER vom spezifischen Benutzer
    ).count()

    context = {
        'article': article, 
        'newspaper': newspaper,
        'public_comments_count': public_comments_count,
    }
    return render(request, 'articles/detailed_article.html', context)

#track newspaper interactions
# @login_required
# def click_newspaper(request, pk):
#     user = request.user
#     ad_obj = get_newspapers.objects.get(id=pk)
#     profile = Profile.objects.get(user=user)

#     if profile not in ad_obj.user_clicked.all():
#         ad_obj.user_clicked.add(profile)

#     ad_obj.num_clicked += 1
#     ad_obj.save()

#     return redirect(ad_obj.url)

