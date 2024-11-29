from allauth.account.forms import SignupForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class CustomSignupForm(SignupForm):
    def save(self, request):
        # Überprüfen, ob der Benutzername bereits existiert
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError(f"Der Benutzername '{username}' ist bereits vergeben.")
        
        user = super().save(request)

        # Setze eine Dummy-E-Mail, falls keine angegeben wurde
        if not user.email:
            user.email = f"{user.username}@example.com"
            user.save()
        
        return user
