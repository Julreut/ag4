from django.contrib import admin
from .models import ExperimentCondition

@admin.register(ExperimentCondition)
class ExperimentConditionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'tag')