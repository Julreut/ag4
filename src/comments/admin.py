from django.contrib import admin
from .models import Comment, PlannedReaction, Like, Dislike

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'content', 'article', 'is_public', 'condition_id', 'created']  # 'condition_id' hinzugefügt
    list_filter = ['is_public', 'article', 'condition_id', 'created']  # 'condition_id' und 'created' hinzugefügt
    search_fields = ['content', 'author__user__username']
    actions = ['make_public', 'make_private', 'set_condition']

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

    def set_condition(self, request, queryset):
        """
        Set a specific 'condition_id' for selected comments.
        Opens a confirmation page where the admin can set a condition ID.
        """
        from django.http import HttpResponseRedirect
        from django.urls import path

        class ConditionSetterForm(admin.helpers.ActionForm):
            condition_id = admin.forms.IntegerField(label="Condition ID", required=True)

        self.action_form = ConditionSetterForm

        def apply_condition(modeladmin, request, queryset):
            condition_id = request.POST.get('condition_id')
            updated = queryset.update(condition_id=condition_id)
            modeladmin.message_user(
                request,
                f"{updated} Kommentare wurden auf die Bedingungs-ID {condition_id} gesetzt."
            )

        return HttpResponseRedirect(request.get_full_path())

    set_condition.short_description = "Set Condition ID for selected comments"


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
