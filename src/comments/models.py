from django.db import models
from django.urls import reverse

from profiles.models import Profile
from articles.models import Article

class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="comments")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")  # Beziehung zum Artikel
    title = models.CharField(max_length=255, default="Default Title")
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=True)  # Gibt an, ob der Kommentar öffentlich ist
    condition_id = models.IntegerField(null=True, blank=True)  # Versuchsbedingungs-ID
    is_secondary = models.BooleanField(default=False)  # Gibt an, ob der Kommentar ein Sekundärkommentar ist
    parent_comment = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE, related_name="replies"
    )
    is_public = models.BooleanField(default=True)
    tag = models.CharField(max_length=50, default='control')

    liked = models.ManyToManyField(Profile, related_name="liked_comments_set", blank=True)
    disliked = models.ManyToManyField(Profile, related_name="disliked_comments_set", blank=True)

    def __str__(self):
        # Kürze den Inhalt auf maximal 50 Zeichen
        content_preview = self.content[:50] + ("..." if len(self.content) > 50 else "")
        return f"{self.title} by {self.author} - {content_preview}"

    class Meta:
        ordering = ['-created']
    
    def get_absolute_url(self):
        return reverse(
            "comments:detailed-comment", 
            kwargs={
                "news_paper_id": self.article.news_paper_id,
                "article_id": self.article.id,
                "comment_id": self.id
            }
        )
