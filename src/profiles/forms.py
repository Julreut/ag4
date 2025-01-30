from django import forms
from .models import Profile
from django.utils.translation import gettext_lazy as _  # Verwendung von `as _` für Konsistenz

class ProfileModelForm(forms.ModelForm):
    bio = forms.CharField(
        label=_("Meine Profilbeschreibung"),
        widget=forms.Textarea(),
        required=False
    )
    avatar = forms.ImageField(
        label=_("Profilbild"),
        help_text = "Empfehlung: 1x1 Format ",
        required=False,
        widget=forms.FileInput  # Überschreibe das Standard-Widget, damit man es nicht mehr zuruecksetzen kann
    )

    class Meta:
        model = Profile
        fields = ('bio', 'avatar')  
