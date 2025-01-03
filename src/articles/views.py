from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse, get_object_or_404
from .models import Article, NewsPaper
from profiles.models import Profile
from django.db.models import Q
from analytics.models import create_event_log

# Create your views here.

## Newspaper definitions
@login_required
def get_newspapers(request):

    ##LOG ENTRY
    create_event_log(
        user=request.user,
        event_type="page_view",
        event_data={"page_type": "newspaper_overview", "id": None}
    )

    news_papers = NewsPaper.objects.all()
    context = {
        'news_papers': news_papers #must use a string
    }
    return render(request, 'articles/news_papers.html', context)

## Article definitions
@login_required
def article_list(request, news_paper_id):
    
    ##LOG ENTRY
    create_event_log(
        user=request.user,
        event_type="page_view",
        event_data={"page_type": "article_list", "id": news_paper_id}
    )

    # Filtere die Artikel basierend auf der Zeitung
    articles = Article.objects.filter(news_paper_id=news_paper_id)
    # Füge die entsprechende Zeitung in den Kontext hinzu
    newspaper = get_object_or_404(NewsPaper, id=news_paper_id)
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

    public_comments_count = article.comments.filter(Q(is_public=True) | Q(author=profile)).count()

    ## LOG ENTRY
    create_event_log(
        user=request.user,
        event_type="article_click",
        event_data={"article_id": article.id}
    )
    
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

