from django.db import models

from django.contrib.auth.models import User


class UserEventLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=100)  # e.g., "article_click", "comment", "page_load"
    event_data = models.TextField(blank=True, null=True)  # e.g., article ID, comment text
    timestamp = models.DateTimeField() ##possible: auto_now_add=True


from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class UserContentPosition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Versuchsperson
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Typ: Article, NewsPaper, Comment
    object_id = models.PositiveIntegerField()  # ID des zugehörigen Objekts (z.B. Artikel-ID)
    content_object = GenericForeignKey('content_type', 'object_id')  # Verknüpfung zum echten Objekt
    position = models.IntegerField()  # Die zufällige Position

    class Meta:
        unique_together = ('user', 'content_type', 'object_id')  # Eindeutige Zuordnung für jeden Benutzer und Inhalt
