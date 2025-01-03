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
    
    
class PlannedReaction(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="planned_reaction_set")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="planned_reactions")
    reaction_type = models.CharField(max_length=10, choices=[("Like", "Like"), ("Dislike", "Dislike")])
    time_delta = models.PositiveIntegerField()  # Zeit in Sekunden bis zur Reaktion

    def __str__(self):
        return f"Planned {self.reaction_type} by {self.user.user.username} on {self.comment.id}"


class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="likes_set")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="likes_on_comment")
    value = models.CharField(max_length=10, choices=[("Like", "Like"), ("Unlike", "Unlike")])

    def __str__(self):
        return f"{self.user.user.username} {self.value} on {self.comment.id}"


class Dislike(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="dislikes_set")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="dislikes_on_comment")
    value = models.CharField(max_length=10, choices=[("Dislike", "Dislike"), ("Undislike", "Undislike")])

    def __str__(self):
        return f"{self.user.user.username} {self.value} on {self.comment.id}"
