# This file stores the sqlite queries required to create the downloadable .xlsx file

def get_query(table):
    if table == "user":
        return """
        SELECT profiles_profile.id AS "user_id", 
               auth_user.username, 
               profiles_profile.first_name, 
               profiles_profile.last_name, 
               profiles_profile.bio, 
               auth_user.date_joined, 
               auth_user.last_login
        FROM profiles_profile
        INNER JOIN auth_user 
        ON profiles_profile.user_id = auth_user.id
        """
    if table == "comments":
        return """
        SELECT comments_comment.id AS "comment_id", 
               comments_comment.author_id, 
               comments_comment.article_id, 
               comments_comment.title, 
               comments_comment.content, 
               comments_comment.created, 
               comments_comment.updated
        FROM comments_comment
        """
    if table == "likes":
        return """
        SELECT comments_like.id AS "like_id", 
               comments_like.user_id, 
               comments_like.comment_id, 
               comments_like.value
        FROM comments_like
        """
    if table == "dislikes":
        return """
        SELECT comments_dislike.id AS "dislike_id", 
               comments_dislike.user_id, 
               comments_dislike.comment_id, 
               comments_dislike.value
        FROM comments_dislike
        """
    if table == "articles":
        return """
        SELECT articles_article.id AS "article_id", 
               articles_article.news_paper_id, 
               articles_article.title, 
               articles_article.content, 
               articles_article.created_at, 
               articles_article.updated_at
        FROM articles_article
        """
    if table == "newspapers":
        return """
        SELECT articles_newspaper.id AS "newspaper_id", 
               articles_newspaper.name, 
               articles_newspaper.image
        FROM articles_newspaper
        """
    if table == "usereventlog":
        return """
        SELECT analytics_usereventlog.id AS "event_id", 
               analytics_usereventlog.user_id, 
               analytics_usereventlog.event_type, 
               analytics_usereventlog.event_data, 
               analytics_usereventlog.timestamp
        FROM analytics_usereventlog
        """
    if table == "usercontentposition":
        return """
        SELECT analytics_usercontentposition.id AS "position_id", 
               analytics_usercontentposition.user_id, 
               analytics_usercontentposition.object_id, 
               analytics_usercontentposition.position
        FROM analytics_usercontentposition
        """
    if table == "experimentcondition":
        return """
        SELECT analytics_experimentcondition.id AS "condition_id", 
               analytics_experimentcondition.name, 
               analytics_experimentcondition.description
        FROM analytics_experimentcondition
        """
    return None
