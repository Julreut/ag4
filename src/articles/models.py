from django.db import models
from django.shortcuts import reverse
import datetime
from django.utils import timezone
from profiles.models import Profile

# Create your models here.

class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    news_paper_id = models.IntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.CharField(max_length=255)
    # num_clicked = models.IntegerField(default=0)
    # user_clicked = models.ManyToManyField(Profile, blank=True, related_name='clicked')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("articles:detailed-article", kwargs={"slug": self.title})
    
    @classmethod
    def get_dummy_articles(cls):
        from io import BytesIO
        from PIL import Image
        from django.core.files.base import ContentFile
        import random
        
        dummy_articles = []
        for i in range(1, 6):
            article = cls(
                id=i,
                title=f"Dummy Article {i}",
                content=f"This is the content of dummy article {i}.",
                created_at=timezone.now() - datetime.timedelta(days=random.randint(1, 10)),
                updated_at=timezone.now(),
                image="https://d1csarkz8obe9u.cloudfront.net/posterpreviews/live-breaking-news-design-template-8c0dbab5f447f2e1e39e0d19d90a5ec7_screen.jpg?ts=1689444194"
            )
            
            
            dummy_articles.append(article)

        # Only use for preview, as it's in-memory and not actually saved to the DB
        return dummy_articles          
    

class NewsPaper(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    # num_clicked = models.IntegerField(default=0)
    # user_clicked = models.ManyToManyField(Profile, blank=True, related_name='clicked')

    def id(self):
        return self.id
    
    def get_absolute_url(self):
        return reverse("", kwargs={"id": self.id})
    