import json

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserEventLog
from profiles.models import Profile
from django.utils.timezone import now

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

