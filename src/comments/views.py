from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView
from django.contrib import messages

from .models import Comment, Like, Dislike, PlannedReaction
from .forms import CommentModelForm, SecondaryCommentModelForm
from profiles.models import Profile
from articles.models import Article, NewsPaper  # Importiere Articles und Newspapers for IDs
from configuration.models import get_the_config

import time


@login_required
def article_comments_view(request, news_paper_id, article_id):
    article = get_object_or_404(Article, id=article_id)
    profile = Profile.objects.get(user=request.user)
    newspaper = get_object_or_404(NewsPaper, id=news_paper_id)

    # Zeige nur öffentliche Kommentare + die des aktuellen Users
    comments = Comment.objects.filter(
        article=article,
        parent_comment=None,
    ).filter(
        Q(is_public=True) | Q(author=profile)
    ).order_by("-created")
    
    comment_form = CommentModelForm()
    secondary_comment_form = SecondaryCommentModelForm()

    # Hauptkommentar hinzufügen
    if request.method == "POST" and 'submit_comment_form' in request.POST:
        comment_form = CommentModelForm(request.POST)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.author = profile
            instance.article = article
            # Standardmäßig ist der Kommentar privat, es sei denn, der Nutzer ist ein Admin
            instance.is_public = request.user.is_staff
            instance.save()
            return redirect('comments:article-comments', news_paper_id=newspaper.id, article_id=article.id)

    # Sekundärkommentar hinzufügen
    if request.method == "POST" and 'submit_secondary_comment_form' in request.POST:
        secondary_comment_form = SecondaryCommentModelForm(request.POST)
        if secondary_comment_form.is_valid():
            instance = secondary_comment_form.save(commit=False)
            instance.author = profile
            instance.article = article
            instance.parent_comment = Comment.objects.get(id=request.POST.get('comment_id'))
            instance.is_public = instance.parent_comment.is_public  # Antworten erben Sichtbarkeit
            instance.save()
            return redirect('comments:article-comments', news_paper_id=newspaper.id, article_id=article.id)

    context = {
        'newspaper': newspaper,
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
        'secondary_comment_form': secondary_comment_form,
    }
    return render(request, 'comments/article_comments.html', context)


@login_required
def like_unlike_comment(request):
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        comment = Comment.objects.get(id=comment_id)
        profile = Profile.objects.get(user=request.user)

        toggle_like(profile, comment)
    return redirect(request.META.get('HTTP_REFERER', 'comments:article-comments'))


@login_required
def dislike_undislike_comment(request):
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        comment = Comment.objects.get(id=comment_id)
        profile = Profile.objects.get(user=request.user)

        toggle_dislike(profile, comment)
    return redirect(request.META.get('HTTP_REFERER', 'comments:article-comments'))


def toggle_like(profile, comment):
    if profile in comment.liked.all():
        comment.liked.remove(profile)
    else:
        comment.liked.add(profile)


def toggle_dislike(profile, comment):
    if profile in comment.disliked.all():
        comment.disliked.remove(profile)
    else:
        comment.disliked.add(profile)

    dislike, created = Dislike.objects.get_or_create(user=profile, comment=comment)
    dislike.value = 'Dislike' if created or dislike.value == 'Undislike' else 'Undislike'
    dislike.save()


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
