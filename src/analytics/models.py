from django.db import models

from profiles.models import Profile
# from posts.models import Post
from django.contrib.auth.models import User


import json
from django.utils.timezone import now


class UserEventLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=100)  # e.g., "article_click", "comment", "page_load"
    event_data = models.TextField(blank=True, null=True)  # e.g., article ID, comment text
    timestamp = models.DateTimeField()
    ##possible: auto_now_add=True


# class TrackedSession(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="tracked_sessions")
#     first_seen = models.DateTimeField(auto_now_add=True)
#     last_seen = models.DateTimeField(auto_now_add=True)

def create_event_log(user, event_type, event_data):
    """
    Erstellt einen UserEventLog-Eintrag mit validierten JSON-Daten.
    
    :param user: Der Benutzer, für den das Event geloggt wird.
    :param event_type: Typ des Events (z. B. 'user_logged_out', 'question_answered').
    :param event_data: Dictionary mit den Event-Daten.
    """
    try:
        # Validierung und Umwandlung der Daten in JSON
        event_data_json = json.dumps(event_data)
        
        # Log-Eintrag erstellen
        UserEventLog.objects.create(
            user=user,
            event_type=event_type,
            event_data=event_data_json,
            timestamp=now() 
        )
    except (TypeError, ValueError) as e:
        print(f"Fehler beim Speichern von Event-Daten: {e}")
