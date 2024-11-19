from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse, get_object_or_404
from .models import Article, NewsPaper
from profiles.models import Profile

# Create your views here.

## Newspaper definitions
@login_required
def get_newspapers(request):
    news1 = NewsPaper(id=1, name="Linke Zeitung", image="https://picsum.photos/id/24/200")
    news2 = NewsPaper(id=2, name="Rechte Zeitung", image="https://picsum.photos/id/3/200")
    news_papers = [news1, news2]
    context = {
        'news_papers': news_papers #must use a string
    }
    return render(request, 'articles/news_papers.html', context)

## Article definitions
@login_required
def article_list(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/all_articles.html', context)

#track article interactions

@login_required
def detailed_article(request, slug):
    # Abrufen des spezifischen Artikels anhand des Slugs
    article = get_object_or_404(Article, slug=slug)

    context = {
        'article': article
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

