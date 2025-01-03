from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.db.models import Q, Prefetch
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView
from django.contrib import messages

from django.http import HttpResponseBadRequest

from .models import Comment, Like, Dislike, PlannedReaction
from .forms import CommentModelForm, SecondaryCommentModelForm
from profiles.models import Profile
from articles.models import Article, NewsPaper  # Importiere Articles und Newspapers for IDs
from configuration.models import get_the_config

from analytics.models import create_event_log

import time

def save_comment(form, profile, article, parent_comment=None, is_public=False):
    """Helper-Funktion zum Speichern von Haupt- und Sekundärkommentaren und Event-Tracking."""
    instance = form.save(commit=False)
    instance.author = profile
    instance.article = article
    instance.parent_comment = parent_comment
    instance.is_public = is_public
    instance.save()

    # Event-Log erstellen
    event_type = "sec_comment_posted" if parent_comment else "main_comment_posted"
    create_event_log(
        user=profile.user,
        event_type=event_type,
        event_data={
            "article_id": article.id,
            "comment_title": instance.title,
            "comment_content": instance.content,
            "parent_comment_id": parent_comment.id if parent_comment else None,
            "is_secondary": parent_comment is not None
        }
    )

    return instance


@login_required
def article_comments_view(request, news_paper_id, article_id):
    article = get_object_or_404(Article, id=article_id)
    profile = Profile.objects.get(user=request.user)
    newspaper = get_object_or_404(NewsPaper, id=news_paper_id)

    ##LOG ENTRY
    create_event_log(
        user=request.user,
        event_type="page_view",
        event_data={"page_type": "article_comments_view", "id": article.id}
    )

    # Hauptkommentare und ihre sekundären Kommentare abrufen
    comments = Comment.objects.filter(
        article=article,
        parent_comment=None,
    ).filter(
        Q(is_public=True) | Q(author=profile)
    ).order_by("-created").prefetch_related(
        Prefetch(
            'replies',  # Sekundäre Kommentare über das rückwärts gerichtete ForeignKey-Attribut
            queryset=Comment.objects.filter(
                Q(is_public=True) | Q(author=profile)
            ).order_by("created"),  # Antworten chronologisch sortieren
            to_attr='loaded_replies'  # Zugriff auf die Antworten über `.loaded_replies`
        )
    )

    comment_form = CommentModelForm()
    secondary_comment_form = SecondaryCommentModelForm()

    # Hauptkommentar hinzufügen
    if request.method == "POST" and 'submit_comment_form' in request.POST:
        comment_form = CommentModelForm(request.POST)
        if comment_form.is_valid():
            save_comment(
                form=comment_form,
                profile=profile,
                article=article,
                is_public=request.user.is_staff  # Admin-Kommentare sind direkt öffentlich
            )
            messages.success(request, _("Dein Kommentar wurde erfolgreich hinzugefügt!"))
            return redirect('comments:article-comments', news_paper_id=newspaper.id, article_id=article.id)
        else:
            messages.error(request, _("Es gab einen Fehler beim Hinzufügen deines Kommentars."))

    # Sekundärkommentar hinzufügen
    if request.method == "POST" and 'submit_secondary_comment_form' in request.POST:
        secondary_comment_form = SecondaryCommentModelForm(request.POST)
        if secondary_comment_form.is_valid():
            parent_comment = get_object_or_404(Comment, id=request.POST.get('comment_id'))
            save_comment(
                form=secondary_comment_form,
                profile=profile,
                article=article,
                parent_comment=parent_comment,
                is_public=False  # Sekundärkommentare sind standardmäßig nicht öffentlich
            )
            messages.success(request, _("Deine Antwort wurde erfolgreich hinzugefügt!"))
            return redirect('comments:article-comments', news_paper_id=newspaper.id, article_id=article.id)
        else:
            messages.error(request, _("Es gab einen Fehler beim Hinzufügen deiner Antwort."))

    context = {
        'newspaper': newspaper,
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
        'secondary_comment_form': secondary_comment_form,
    }
    return render(request, 'comments/article_comments.html', context)


@login_required
def detailed_comment_view(request, news_paper_id, article_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    article = get_object_or_404(Article, id=article_id)
    profile = Profile.objects.get(user=request.user)
    newspaper = get_object_or_404(NewsPaper, id=news_paper_id)
    replies = comment.replies.filter(Q(is_public=True) | Q(author=profile))

    ##LOG ENTRY
    create_event_log(
        user=request.user,
        event_type="page_view",
        event_data={"page_type": "detailed_comment_view", "id": comment.id}
    )

    # Sekundärkommentar hinzufügen
    if request.method == "POST" and 'submit_secondary_comment_form' in request.POST:
        form = SecondaryCommentModelForm(request.POST)
        if form.is_valid():
            save_comment(
                form=form,
                profile=profile,
                article=article,
                parent_comment=comment,
                is_public=request.user.is_staff  # Antworten von Admins sind direkt öffentlich
            )
            messages.success(request, _("Deine Antwort wurde erfolgreich hinzugefügt!"))
            return redirect('comments:detailed-comment', comment_id=comment_id, news_paper_id=newspaper.id, article_id=article.id)
        else:
            messages.error(request, _("Es gab einen Fehler beim Hinzufügen deiner Antwort."))

    context = {
        'comment': comment,
        'replies': replies,
        'article': article,
        'newspaper': newspaper,
        'secondary_comment_form': SecondaryCommentModelForm(),
    }

    return render(request, 'comments/detailed_comment.html', context)

@login_required
def like_unlike_comment(request):
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        comment = Comment.objects.get(id=comment_id)
        profile = Profile.objects.get(user=request.user)

        # Call the updated toggle_like function with logging
        toggle_like(profile, comment, request)

    return redirect(request.META.get('HTTP_REFERER', 'comments:article-comments'))


@login_required
def dislike_undislike_comment(request):
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        comment = Comment.objects.get(id=comment_id)
        profile = Profile.objects.get(user=request.user)

        # Call the updated toggle_dislike function with logging
        toggle_dislike(profile, comment, request)

    return redirect(request.META.get('HTTP_REFERER', 'comments:article-comments'))


def toggle_like(profile, comment, request):
    if profile in comment.liked.all():
        # If already liked, remove like
        comment.liked.remove(profile)
        # Log event for unlike
        create_event_log(
            user=request.user,
            event_type="comment_unliked",
            event_data={
                "comment_id": comment.id,
                "comment_title": comment.title,
                "author": comment.author.user.username
            }
        )
    else:
        # Add like
        comment.liked.add(profile)
        # Remove dislike if exists
        if profile in comment.disliked.all():
            comment.disliked.remove(profile)
        # Log event for like
        create_event_log(
            user=request.user,
            event_type="comment_liked",
            event_data={
                "comment_id": comment.id,
                "comment_title": comment.title,
                "author": comment.author.user.username
            }
        )


def toggle_dislike(profile, comment, request):
    if profile in comment.disliked.all():
        # If already disliked, remove dislike
        comment.disliked.remove(profile)
        # Log event for undislike
        create_event_log(
            user=request.user,
            event_type="comment_undisliked",
            event_data={
                "comment_id": comment.id,
                "comment_title": comment.title,
                "author": comment.author.user.username
            }
        )
    else:
        # Add dislike
        comment.disliked.add(profile)
        # Remove like if exists
        if profile in comment.liked.all():
            comment.liked.remove(profile)
        # Log event for dislike
        create_event_log(
            user=request.user,
            event_type="comment_disliked",
            event_data={
                "comment_id": comment.id,
                "comment_title": comment.title,
                "author": comment.author.user.username
            }
        )


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    """Ermöglicht das Löschen eigener Kommentare."""
    model = Comment
    template_name = 'comments/confirm_del.html'
    success_url = reverse_lazy('comments:article-comments')

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = Comment.objects.get(pk=pk)
        if obj.author != Profile.objects.get(user=self.request.user):
            messages.warning(self.request, _("You are not allowed to delete this comment."))
        return obj


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    """Ermöglicht das Aktualisieren eigener Kommentare."""
    form_class = CommentModelForm
    model = Comment
    template_name = 'comments/update.html'
    success_url = reverse_lazy('comments:article-comments')

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        if form.instance.author == profile:
            return super().form_valid(form)
        else:
            form.add_error(None, _("You are not allowed to edit this comment."))
            return super().form_invalid(form)


def process_planned_reactions(profile):
    """Verarbeitet geplante Reaktionen."""
    executed_reactions = []
    for planned_reaction in PlannedReaction.objects.filter(target_profile=profile):
        comment = planned_reaction.comment

        if time.time() - comment.created.timestamp() > planned_reaction.time_delta:
            if planned_reaction.reaction_type == "Like":
                toggle_like(profile, comment)
            elif planned_reaction.reaction_type == "Dislike":
                toggle_dislike(profile, comment)

            executed_reactions.append(planned_reaction.id)

    PlannedReaction.objects.filter(id__in=executed_reactions).delete()
