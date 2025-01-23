from django.contrib import admin

# Register your models here.
from configuration.models import Configuration


# unloading modules to hide them from the admin panel, this app is loaded AFTER allauth, so it can unregister
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken
from django.contrib import admin

admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.unregister(EmailAddress)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(SocialToken)


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = [
        "like_dislike_enabled",
        "registration_enabled",
        "is_timer_enabled",  # Timer aktiviert?
        "max_session_duration",  # Maximale Sitzungsdauer
        "management_token",
    ]
    fields = [
        "like_dislike_enabled",
        "registration_enabled",
        "is_timer_enabled",
        "max_session_duration",
        "management_token",
    ]

    def change_configuration(self, configuration):
        return "change configuration"

