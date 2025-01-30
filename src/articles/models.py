from django.db import models
from django.shortcuts import reverse
import datetime
import itertools
from django.utils import timezone
from profiles.models import Profile
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify



# Create your models here.

class Article(models.Model):
    # id = models.IntegerField(primary_key=True)
    news_paper_id = models.IntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True)  # Slug-Feld hinzugefügt
    image = models.ImageField(upload_to='articles', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=False, help_text= "Format am besten einheitlich. Empfehlung Bannerformat:1800 x 600 px")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.CharField(max_length=50, default='', blank=True)  #optional Tag für die Versuchsbedingung
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Slug nur generieren, wenn es noch leer ist
            base_slug = slugify(self.title)
            slug = base_slug
            for i in itertools.count(1):  # Konflikte mit anderen Slugs vermeiden
                if not Article.objects.filter(slug=slug).exists():
                    break
                slug = f"{base_slug}-{i}"
            self.slug = slug
        super().save(*args, **kwargs)  # Standard-Save-Methode
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('articles:detailed-article', kwargs={'news_paper_id': self.news_paper_id, 'slug': self.slug})

    
class NewsPaper(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=255, default = 'Change me: This is the short description of the newspaper content.')
    image = models.ImageField(upload_to='articles', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=False, help_text= "Format am besten einheitlich. Empfehlung Format:900 x 600 px")
    tag = models.CharField(max_length=50, default='', blank=True)  #optional Tag für die Versuchsbedingung
    def get_id(self):
        return self.id

    def get_absolute_url(self):
        return reverse("all-articles", kwargs={"news_paper_id": self.id})
