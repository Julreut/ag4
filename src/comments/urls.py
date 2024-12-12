from django.urls import path
from .views import (
    CommentDeleteView,
    CommentUpdateView,
    like_unlike_comment,
    dislike_undislike_comment,
    article_comments_view,
    detailed_comment_view,
)

app_name = 'comments'

urlpatterns = [
    path('article/<int:news_paper_id>/<int:article_id>/', article_comments_view, name='article-comments'),  # Neue Route
    path('<int:news_paper_id>/<int:article_id>/<int:comment_id>/', detailed_comment_view, name='detailed-comment'),
    path('liked/', like_unlike_comment, name='like-comment-view'),
    path('disliked/', dislike_undislike_comment, name='dislike-comment-view'),
    path('<pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('<pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
]
