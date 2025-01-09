from django.contrib import admin
from django import forms

from .models import Comment, PlannedReaction, Like, Dislike
from analytics.models import ExperimentCondition


class CommentAdminForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamische Dropdown-Werte aus der ExperimentCondition-Tabelle
        self.fields['tag'].widget = forms.Select(
            choices=[(condition.tag, condition.name) for condition in ExperimentCondition.objects.all()]
        )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'content', 'article', 'is_public', 'created']  # 'condition_id' hinzugefügt
    list_filter = ['is_public', 'article','created']  # 'condition_id' und 'created' hinzugefügt
    search_fields = ['content', 'author__user__username']
    actions = ['make_public', 'make_private']
    form = CommentAdminForm  # Verwende das benutzerdefinierte Formular


    def make_public(self, request, queryset):
        """
        Set the 'is_public' field to True for selected comments.
        """
        updated = queryset.update(is_public=True)
        self.message_user(request, f"{updated} ausgewählte Kommentare wurden öffentlich gemacht.")

    def make_private(self, request, queryset):
        """
        Set the 'is_public' field to False for selected comments.
        """
        updated = queryset.update(is_public=False)
        self.message_user(request, f"{updated} ausgewählte Kommentare wurden privat gemacht.")


@admin.register(PlannedReaction)
class PlannedReactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'comment', 'reaction_type', 'time_delta']
    list_filter = ['reaction_type']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'comment', 'value']
    list_filter = ['value']


@admin.register(Dislike)
class DislikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'comment', 'value']
    list_filter = ['value']

