from django.shortcuts import render
from .models import create_event_log

# Create your views here.

## Backend view for json time tracking
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def log_time_spent(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            page_type = data.get("page_type")
            page_id = data.get("id")
            duration_ms = data.get("duration_ms")

            # Log-Eintrag erstellen
            create_event_log(
                user=request.user,
                event_type="time_spent",
                event_data={
                    "page_type": page_type,
                    "id": page_id,
                    "duration_ms": duration_ms
                }
            )
            return JsonResponse({"status": "success"})
        except Exception as e:
            print(f"Fehler beim Verarbeiten der Zeitdaten: {e}")
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)