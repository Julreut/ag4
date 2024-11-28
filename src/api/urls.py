from django.urls import path
from .views import create_user, modify_relationship, create_delete_post, modify_reaction, create_delete_advertisement, create_delete_article, create_delete_comment

## Das sind REQUEST Urls, einfügen in Postman oder über Swagger ins Terminal einfügen
app_name = "api"

urlpatterns = [
    path('user', create_user, name='create-user'),
    path('profile/comment/', create_delete_comment, name='create-delete-comment'),
    path('profile/relationship', modify_relationship, name='modify-relationship'),
    path('profile/post', create_delete_post, name='create-delete-post'),
    path('profile/post/reaction', modify_reaction, name='modify-reaction'),
    path('advertisement', create_delete_advertisement, name='create-delete-advertisement'),
    path('article', create_delete_article, name='create-delete-article'),
]
