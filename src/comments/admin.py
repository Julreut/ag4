from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError

from .models import Comment
from analytics.models import ExperimentCondition


class CommentAdminForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamische Dropdown-Werte aus der ExperimentCondition-Tabelle
        self.fields['tag'].widget = forms.Select(
            choices=[("", "Keine Condition auswählen")]+
            [(condition.tag, condition.name) for condition in ExperimentCondition.objects.all()]
        )
        # Filtere nur Hauptkommentare für das Feld `parent_comment`
        self.fields['parent_comment'].queryset = Comment.objects.filter(parent_comment=None)

        if self.instance and self.instance.is_secondary:
            self.fields['liked'].widget.attrs['disabled'] = True
            self.fields['disliked'].widget.attrs['disabled'] = True

            
    def clean(self):
        cleaned_data = super().clean()
        is_secondary = cleaned_data.get('is_secondary')
        parent_comment = cleaned_data.get('parent_comment')

        # Sekundärer Kommentar benötigt einen Parent-Kommentar
        if is_secondary and not parent_comment:
            raise ValidationError("Ein sekundärer Kommentar muss einen übergeordneten Kommentar haben.")

        # Hauptkommentar darf keinen Parent-Kommentar haben
        if not is_secondary and parent_comment:
            raise ValidationError("Ein Hauptkommentar darf keinen übergeordneten Kommentar haben.")


        return cleaned_data
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
