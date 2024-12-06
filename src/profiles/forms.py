from django import forms
from .models import Profile
from django.utils.translation import ugettext_lazy as _  # Verwendung von `as _` für Konsistenz

class ProfileModelForm(forms.ModelForm):
    bio = forms.CharField(
        label=_("My Profile Biography"),
        widget=forms.Textarea(),
        required=False
    )
    avatar = forms.ImageField(
        label=_("Profile Picture"),
        required=False
    )

    class Meta:
        model = Profile
        fields = ('bio', 'avatar')  
