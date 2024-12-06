from django.urls import path
from .views import create_user, create_delete_article, create_delete_comment

## Das sind REQUEST Urls, einfügen in Postman oder über Swagger ins Terminal einfügen
app_name = "api"

urlpatterns = [
    path('user', create_user, name='create-user'),
    path('profile/comment/', create_delete_comment, name='create-delete-comment'),
    path('article', create_delete_article, name='create-delete-article'),
]
