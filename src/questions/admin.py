from django.contrib import admin
from .models import Question, Text


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name','question_text', 'question_type', 'label','required', 'order')
    list_editable = ("order",)
    ordering = ("order",)
    search_fields = ('question_text',)
    list_filter = ('label', 'question_type', 'required')
    ordering = ('label', 'question_type')
    fields = (
        'name',
        'question_type',
        'required',
        'order',
        'label', 
        'question_text', 
        'choices', 
        'sub_questions',
        'sub_choices',
        'min_value', 
        'max_value',
        'start_value', 
        'step_value', 
        'range_value'
    )

    def get_queryset(self, request):
        # Allow admin to filter questions based on label and type
        queryset = super().get_queryset(request)
        return queryset

    def save_model(self, request, obj, form, change):
        # Log changes for better debugging
        if change:
            print(f"Updated question: {obj}")
        else:
            print(f"Created new question: {obj}")
        super().save_model(request, obj, form, change)

# Admin configuration for Text model
from django.contrib import admin

@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'content_preview', 'visibility')
    search_fields = ('identifier', 'content')
    ordering = ('identifier',)
    list_filter = ('identifier', 'visibility')
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
