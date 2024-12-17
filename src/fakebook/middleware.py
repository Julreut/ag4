from datetime import timedelta, datetime
from django.utils.timezone import now
from django.contrib.auth import logout
from django.shortcuts import redirect
from questions.models import SessionConfig

class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Konfiguration aus der Datenbank laden
            config = SessionConfig.objects.first()

            # Timer aktivieren, wenn is_timer_enabled = True
            if config and config.is_timer_enabled:
                max_session_duration = config.max_duration if config else 3600

                # Wenn "/newspapers/" besucht wird, Startzeit einmal setzen
                if request.path == '/newspapers/':
                    if 'newspaper_entry_time' not in request.session:
                        request.session['newspaper_entry_time'] = now().isoformat()

                # Timer prüfen, wenn die Startzeit gesetzt wurde
                newspaper_entry_time = request.session.get('newspaper_entry_time')
                if newspaper_entry_time:
                    newspaper_entry_time = datetime.fromisoformat(newspaper_entry_time)
                    if now() - newspaper_entry_time > timedelta(seconds=max_session_duration):
                        # Logout und Weiterleitung zur Endseite
                        logout(request)
                        return redirect('/questions/end')
            else:
                # Wenn der Timer deaktiviert ist, Eintrag entfernen
                if 'newspaper_entry_time' in request.session:
                    del request.session['newspaper_entry_time']

        response = self.get_response(request)
        return response
