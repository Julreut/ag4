from django.db import models

from django.contrib.auth.models import User


class UserEventLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=100)  # e.g., "article_click", "comment", "page_load"
    event_data = models.TextField(blank=True, null=True)  # e.g., article ID, comment text
    timestamp = models.DateTimeField() ##possible: auto_now_add=True


   