from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile  # Profile ist in der gleichen App
from questions.models import Consent  # Importiere Consent aus der richtigen App

@receiver(post_save, sender=User)
def post_save_create_profile_and_consent(sender, instance, created, **kwargs):
    if created:
        # Erstelle das Profile
        Profile.objects.create(user=instance)
        
        # Erstelle den Consent (aus der App 'questions')
        Consent.objects.create(user=instance, consent_given=True)


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