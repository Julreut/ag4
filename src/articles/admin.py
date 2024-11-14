from django.contrib import admin
from .models import NewsPaper, Article
from fakebook.downloads import get_csv

@admin.register(NewsPaper)
class NewsPaperAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    # list_display = ['id', 'image', 'text', 'url', 'num_clicked']

    def download_csv(self, request, queryset):
        response = get_csv(self.list_display, queryset, 'newspaper.csv')
        return response

    download_csv.short_description = "Download CSV file"

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    # list_display = ['id', 'image', 'text', 'url', 'num_clicked']

    def download_csv(self, request, queryset):
        response = get_csv(self.list_display, queryset, 'newspaper.csv')
        return response

    download_csv.short_description = "Download CSV file"