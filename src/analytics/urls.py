from django.urls import path
from .views import log_time_spent

app_name = 'analytics'

urlpatterns = [
    path('log_time_spent/', log_time_spent, name='log_time_spent'),
]
