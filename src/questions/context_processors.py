from django.conf import settings
from .models import SessionConfig


def global_settings(request):
    return {
        'LOGOUT_REDIRECT_URL': settings.LOGOUT_REDIRECT_URL,
    }

def session_config(request):
    config = SessionConfig.objects.first()
    return {
        'MAX_SESSION_DURATION': config.max_duration if config else 3600  # Fallback: 1 Stunde
    }