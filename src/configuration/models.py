import random
import string

from django.db import models

class Configuration(models.Model):
    like_dislike_enabled = models.BooleanField(default=True)
    registration_enabled = models.BooleanField(default=True)
    management_token = models.CharField(default="changeme", max_length=100)
    is_timer_enabled = models.BooleanField(default=False)  # Neues Feld für Timer
    max_session_duration = models.PositiveIntegerField(default=3600)  # Maximale Dauer in Sekunden (Standard: 1 Stunde)

    def regenerate_mgmt_token(self):
        self.management_token = "".join([random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(16)])
        self.save()



def get_the_config() -> Configuration:
    config = Configuration.objects.first()
    if config is None:
        print("Config not found! Creating config...")
        config = Configuration.objects.create(
            like_dislike_enabled=True,
            is_timer_enabled=False,
            max_session_duration=1800,  # Standard: halbe Stunde
        )
    if config.management_token == "changeme":
        config.regenerate_mgmt_token()
    return config

def ensure_config_exists():
    c = get_the_config()
    if not c:
        raise RuntimeError("Could not create configuration")