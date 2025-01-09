from django.contrib import admin
from django import forms

from .models import NewsPaper, Article
from fakebook.downloads import get_csv

from analytics.models import ExperimentCondition

class NewsPaperAdminForm(forms.ModelForm):
    class Meta:
        model = NewsPaper
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamische Dropdown-Werte aus der ExperimentCondition-Tabelle
        self.fields['tag'].widget = forms.Select(
            choices=[(condition.tag, condition.name) for condition in ExperimentCondition.objects.all()]
        )

@admin.register(NewsPaper)
class NewsPaperAdmin(admin.ModelAdmin):
    form = NewsPaperAdminForm  # Verwende das benutzerdefinierte Formular
    actions = ['download_csv']
    # list_display = ['id', 'image', 'text', 'url', 'num_clicked']

    def download_csv(self, request, queryset):
        response = get_csv(self.list_display, queryset, 'newspaper.csv')
        return response

    download_csv.short_description = "Download CSV file"

class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = NewsPaper
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamische Dropdown-Werte aus der ExperimentCondition-Tabelle
        self.fields['tag'].widget = forms.Select(
            choices=[(condition.tag, condition.name) for condition in ExperimentCondition.objects.all()]
        )

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    actions = ['download_csv']
    # list_display = ['id', 'image', 'text', 'url', 'num_clicked']

    def download_csv(self, request, queryset):
        response = get_csv(self.list_display, queryset, 'newspaper.csv')
        return response

    download_csv.short_description = "Download CSV file"
