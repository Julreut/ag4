from django.shortcuts import render
from .utils import create_event_log

# Create your views here.

## Backend view for json time tracking KLAPPT NOCH NICHT
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def log_user_action(request):
    """
    Loggt Javascript Benutzeraktionen wie 'Mehr lesen', 'Weniger lesen' oder 'Antwort schreiben'.
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user = request.user if request.user.is_authenticated else None
            event_type = data.get("event_type")
            event_data = data.get("event_data", {})

            # Logging überspringen für anonyme Benutzer
            if not user:
                print("Skipping logging: User is anonymous.")
                return JsonResponse({"message": "Event logging skipped for anonymous user"}, status=200)
            
            
          # Zusätzliche Validierung actions
            if event_type in ["click"] and "action" in event_data:
                action = event_data.get("action")
                if action not in ["like", "unlike", "dislike", "undislike", "read_and_interact"]:
                    return render(request, "404.html", status=404)
                
            # Event loggen
            create_event_log(user, event_type, event_data)
            
            return JsonResponse({"message": "Event erfolgreich geloggt"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)