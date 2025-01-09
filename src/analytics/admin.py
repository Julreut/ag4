from django.contrib import admin
from .models import ExperimentCondition

@admin.register(ExperimentCondition)
class ExperimentConditionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'tag')



# from django.contrib import admin

# from analytics.models import TrackedSession
# from fakebook.downloads import get_csv


# @admin.register(TrackedSession)
# class TrackedSessionAdmin(admin.ModelAdmin):
#     actions = ['download_csv']
#     list_display = ['username', 'duration', 'first_seen', 'last_seen']

#     def download_csv(self, request, queryset):
#         response = get_csv(self.list_display, queryset, 'sessions.csv')
#         return response

#     def username(self, session):
#         return session.profile.user.username

#     def duration(self, session):
#         return session.last_seen - session.first_seen

#     download_csv.short_description = "Download CSV file"
