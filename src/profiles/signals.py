from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.timezone import now
from .models import Profile, ExperimentCondition
from questions.models import Consent
from analytics.utils import create_event_log
import random


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

@receiver(user_logged_in)
def assign_condition_on_login(sender, request, user, **kwargs):
    # Hole das zugehörige Profile-Objekt
    profile = Profile.objects.filter(user=user).first()

    if profile and not profile.condition:
        conditions = ExperimentCondition.objects.all()
        condition_assigned = None  # Initialisierung

        if conditions.exists():
            condition_assigned = random.choice(conditions)
            profile.condition = condition_assigned
        else:
            # 1. Condition erstellen UND speichern
            first_condition = ExperimentCondition(
                name="FirstCond", 
                description="Eine Test-Bedingung", 
                tag="ChangeMe"
            )
            first_condition.save()  #WICHTIG: Speichern vor Zuweisung
            condition_assigned = first_condition  #Für das Logging
            profile.condition = first_condition

        profile.save()  # 2. Profil erst NACH dem Speichern der Condition speichern

        # Logge das Zuweisungsereignis
        create_event_log(
            user=user,
            event_type="condition_assigned",
            event_data={"condition": condition_assigned.name}
        )

    # Setze die Login-Zeit
    request.session['login_time'] = now().isoformat()

    # Logge das Login-Event
    create_event_log(
        user=user,
        event_type="user_logged_in",
        event_data={"ip_address": get_client_ip(request)}  # IP-Adresse des Nutzers
    )

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    # Logge das Logout-Ereignis
    create_event_log(
        user=request.user,
        event_type="user_logged_out",
        event_data={"logout_time": now().isoformat()}
    )


# Hilfsfunktion, um die IP-Adresse des Nutzers zu bekommen
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
