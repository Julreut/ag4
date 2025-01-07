from .models import UserEventLog

def calculate_questionnaire_duration(user, label):
    start_event = UserEventLog.objects.filter(
        user=user,
        event_type=f"{label}_questions_started"
    ).first()

    end_event = UserEventLog.objects.filter(
        user=user,
        event_type=f"{label}_questions_completed"
    ).first()

    if start_event and end_event:
        duration = (end_event.timestamp - start_event.timestamp).total_seconds()
        return duration
    return None
