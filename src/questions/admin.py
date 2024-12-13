from django.contrib import admin
from .models import Question, Text, SessionConfig


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'question_type', 'label', 'required')
    list_filter = ('question_type', 'label', 'required')
    search_fields = ('question_text',)

    fieldsets = (
        (None, {
            'fields': ('label', 'question_text', 'question_type', 'required')
        }),
        ('Zusätzliche Optionen', {
            'fields': ('choices', 'min_value', 'max_value'),
            'description': 'Diese Felder werden je nach Fragetyp benötigt.'
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        """Fragetyp nach Erstellung nicht mehr änderbar."""
        if obj:
            return ['question_type']
        return []

    def get_fields(self, request, obj=None):
        """Angezeigte Felder dynamisch anpassen."""
        fields = super().get_fields(request, obj)
        if obj:
            if obj.question_type in ['dropdown', 'likert', 'multiple_choice', 'single_choice']:
                return ('label', 'question_text', 'question_type', 'required', 'choices')
            elif obj.question_type == 'numeric':
                return ('label', 'question_text', 'question_type', 'required', 'min_value', 'max_value')
            else:
                return ('label', 'question_text', 'question_type', 'required')
        return fields

# Admin configuration for Text model
from django.contrib import admin

@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'content_preview', 'visibility')
    search_fields = ('identifier', 'content')
    ordering = ('identifier',)
    fields = ('identifier', 'content', 'visibility')  # Customize the detail view order

    def content_preview(self, obj):
        # Truncate the content for preview purposes
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Content Preview'

    def get_queryset(self, request):
        # Include a display of all unique identifiers for admin reference
        queryset = super().get_queryset(request)
        identifiers = queryset.values_list('identifier', flat=True).distinct()
        print("Available Identifiers:", list(identifiers))  # Log the identifiers for the admin
        return queryset

@admin.register(SessionConfig)
class SessionConfigAdmin(admin.ModelAdmin):
    list_display = ('max_duration',)
