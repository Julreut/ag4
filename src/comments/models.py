from django.db import models
from profiles.models import Profile
from articles.models import Article

class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="comments")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")  # Beziehung zum Artikel
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    parent_comment = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE, related_name="replies"
    )
    is_public = models.BooleanField(default=True)

    liked = models.ManyToManyField(Profile, related_name="liked_comments_set", blank=True)
    disliked = models.ManyToManyField(Profile, related_name="disliked_comments_set", blank=True)

    def __str__(self):
        return f"{self.author.user.username}: {self.content[:20]}"

    class Meta:
        ordering = ['-created']

        
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
