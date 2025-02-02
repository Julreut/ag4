from django.contrib import admin
from .models import Profile
from fakebook.downloads import get_csv


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    list_display = ['user', 'condition', 'bio', 'slug', 'id']  # Adjusted fields to match the simplified Profile model

    def download_csv(self, request, queryset):
        response = get_csv(self.list_display, queryset, 'profiles.csv')
        return response

    download_csv.short_description = "Download CSV file"