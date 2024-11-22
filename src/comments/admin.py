from django.contrib import admin
from .models import Comment, PlannedReaction, Like, Dislike
from fakebook.downloads import get_csv

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'content', 'article', 'is_public', 'created']
    list_filter = ['is_public', 'article']
    search_fields = ['content', 'author__user__username']
    actions = ['make_public', 'make_private']

    def make_public(self, request, queryset):
        queryset.update(is_public=True)
        self.message_user(request, "Ausgewählte Kommentare wurden öffentlich gemacht.")

    def make_private(self, request, queryset):
        queryset.update(is_public=False)
        self.message_user(request, "Ausgewählte Kommentare wurden privat gemacht.")

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
