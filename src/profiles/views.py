from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post
from .models import Profile
from .forms import ProfileModelForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from comments.models import Comment


from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Profile
from comments.models import Comment  # Importiere das Comment-Modell
from .forms import ProfileModelForm

@login_required
def my_profile_view(request, slug=None):
    # Hol das Profil basierend auf dem Slug oder das eigene Profil
    if slug:
        profile = get_object_or_404(Profile, slug=slug)
    else:
        profile = Profile.objects.get(user=request.user)

    # Profilbearbeitungsformular nur für den aktuellen Benutzer
    form = None
    confirm = False
    if profile.user == request.user:
        form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
        if request.method == "POST" and form.is_valid():
            form.save()
            confirm = True

    # Kommentare: Alle für den Profilbesitzer, nur öffentliche für andere
    if profile.user == request.user:
        comments = Comment.objects.filter(author=profile)
    else:
        comments = Comment.objects.filter(author=profile, is_public=True)

    # Kontextdaten
    context = {
        'profile': profile,
        'form': form,
        'confirm': confirm,
        'comments': comments,
    }
    return render(request, 'profiles/myprofile.html', context)

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profiles/detail.html'

    def get_object(self, slug=None):
        slug = self.kwargs.get('slug')
        profile = get_object_or_404(Profile, slug=slug)
        return profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        # Füge die gewünschten Daten zum Kontext hinzu
        context["username"] = profile.user.username
        context["bio"] = profile.bio
        # Kommentare filtern: Alle Kommentare für den Profilbesitzer, nur öffentliche für andere
        if self.request.user == profile.user:
            context["comments"] = Comment.objects.filter(author=profile)  # Filtere nach dem User
        else:
            context["comments"] = Comment.objects.filter(author=profile, is_public=True)  # Nur öffentliche Kommentare
        return context

class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.exclude(user=self.request.user)

