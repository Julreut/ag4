from django.urls import path
from .views import (
    participant_info,
    redirect_to_questions,
    question_list,
    experiment_start,
    experiment_end,
    consent_form,
    not_eligible,
    custom_login_view,
)

app_name = 'questions'

urlpatterns = [
    path('start/', experiment_start, name='experiment_start'),
    path('participant_info/', participant_info, name='participant_info'),
    path('consent-form/', consent_form, name='consent_form'),
    path('not_eligible/', not_eligible, name='not_eligible'),
    path('redirect_to_questions/', redirect_to_questions, name='redirect_to_questions'),
    path('before/', question_list, {'label': 'before'}, name='questions_before'),
    path('after/', question_list, {'label': 'after'}, name='questions_after'),
    path('end/', experiment_end, name='experiment_end'),

    path('custom_login_view/', custom_login_view, name='custom_login_view'),


]
