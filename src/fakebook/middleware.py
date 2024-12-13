from datetime import timedelta
from django.utils.timezone import now
from django.contrib.auth import logout
from django.shortcuts import redirect
from questions.models import SessionConfig

class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Maximal erlaubte Zeit aus der Datenbank holen
            config = SessionConfig.objects.first()
            max_session_duration = config.max_duration if config else 3600  # Fallback: 1 Stunde

            # Login-Zeit aus der Session holen oder setzen
            login_time = request.session.get('login_time', None)
            if not login_time:
                request.session['login_time'] = now().isoformat()
            else:
                login_time = now().fromisoformat(login_time)
                if now() - login_time > timedelta(seconds=max_session_duration):
                    logout(request)
                    return redirect('/questions/end')  # Zielseite nach Ablauf

        response = self.get_response(request)
        return response



