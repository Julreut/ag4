from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile  # Profile ist in der gleichen App
from questions.models import Consent  # Importiere Consent aus der richtigen App
from django.contrib.auth.signals import user_logged_in
from django.utils.timezone import now
from analytics.models import UserEventLog
from django.contrib.auth.signals import user_logged_out

import json
from analytics.models import create_event_log

@receiver(post_save, sender=User)
def post_save_create_profile_and_consent(sender, instance, created, **kwargs):
    if created:
        # Erstelle das Profile
        Profile.objects.create(user=instance)
        
        # Erstelle den Consent (aus der App 'questions')
        Consent.objects.create(user=instance, consent_given=True)

        # Logge das Event der Benutzererstellung
        create_event_log(
            user=instance,
            event_type="account_created",
            event_data={"username": instance.username}
        )

def set_login_time(sender, request, user, **kwargs):
    print(f"User {user} logged in at {now().isoformat()}")  # Debugging-Ausgabe
    # Speichere Login-Zeit in die Session
    request.session['login_time'] = now().isoformat()
    
    # Logge das Login-Event
    create_event_log(
        user=user,
        event_type="user_logged_in",
        event_data={"ip_address": get_client_ip(request)} # JSON in String umwandeln
    )

    # Hilfsfunktion, um die IP-Adresse des Nutzers zu bekommen
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


user_logged_in.connect(set_login_time)

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    create_event_log(
        user=request.user,
        event_type="user_logged_out",
        event_data={"logout_time": now().isoformat()}
    )


# @receiver(post_save, sender=Relationship)
# def post_save_add_to_friends(sender, instance, created, **kwargs):
#     sender_ = instance.sender
#     receiver_ = instance.receiver
#     if instance.status == 'accepted':
#         sender_.friends.add(receiver_.user)
#         receiver_.friends.add(sender_.user)
#         sender_.save()
#         receiver_.save()

# @receiver(pre_delete, sender=Relationship)
# def pre_delete_remove_from_friends(sender, instance, **kwargs):
#     sender = instance.sender
#     receiver = instance.receiver
#     sender.friends.remove(receiver.user)
#     receiver.friends.remove(sender.user)
#     sender.save()
#     receiver.save()