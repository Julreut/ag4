from django.urls import path
from .views import log_user_action

app_name = 'analytics'

urlpatterns = [
    path("log-action/", log_user_action, name="log_user_action"),
]
