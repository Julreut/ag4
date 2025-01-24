# This file stores the sqlite queries required to create the downloadable .xlsx file
def get_query(table):
    if table == "user":
        return """
        SELECT auth_user.id AS "user_id", 
               auth_user.username, 
               auth_user.first_name, 
               auth_user.last_name, 
               auth_user.email, 
               auth_user.is_staff, 
               auth_user.is_active, 
               auth_user.is_superuser, 
               auth_user.last_login, 
               auth_user.date_joined
        FROM auth_user
        """
    if table == "comments":
        return """
        SELECT comments_comment.id AS "comment_id", 
               comments_comment.author_id, 
               comments_comment.article_id, 
               comments_comment.title, 
               comments_comment.content, 
               comments_comment.created, 
               comments_comment.updated, 
               comments_comment.public, 
               comments_comment.is_secondary, 
               comments_comment.parent_comment_id, 
               comments_comment.is_public, 
               comments_comment.tag
        FROM comments_comment
        """
    if table == "likes":
        return """
        SELECT comments_comment_liked.id AS "like_id", 
               comments_comment_liked.profile_id,
               comments_comment_liked.comment_id
        FROM comments_comment_liked
        """
    if table == "dislikes":
        return """
        SELECT comments_comment_disliked.id AS "dislike_id", 
               comments_comment_disliked.profile_id, 
               comments_comment_disliked.comment_id
        FROM comments_comment_disliked
        """
    if table == "articles":
        return """
        SELECT articles_article.id AS "article_id", 
               articles_article.news_paper_id, 
               articles_article.title, 
               articles_article.content, 
               articles_article.slug, 
               articles_article.image, 
               articles_article.created_at, 
               articles_article.updated_at, 
               articles_article.tag
        FROM articles_article
        """
    if table == "newspapers":
        return """
        SELECT articles_newspaper.id AS "newspaper_id", 
               articles_newspaper.name, 
               articles_newspaper.image, 
               articles_newspaper.tag
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
               analytics_usercontentposition.content_type_id, 
               analytics_usercontentposition.object_id, 
               analytics_usercontentposition.position
        FROM analytics_usercontentposition
        """
    if table == "experimentcondition":
        return """
        SELECT analytics_experimentcondition.id AS "condition_id", 
               analytics_experimentcondition.name, 
               analytics_experimentcondition.description, 
               analytics_experimentcondition.tag
        FROM analytics_experimentcondition
        """
    if table == "questions":
        return """
        SELECT questions_question.id AS "question_id", 
               questions_question.name, 
               questions_question.question_type, 
               questions_question.label, 
               questions_question.question_text, 
               questions_question.choices, 
               questions_question.sub_questions, 
               questions_question.min_value, 
               questions_question.max_value, 
               questions_question.step_value, 
               questions_question.required
        FROM questions_question
        """
    if table == "answers":
        return """
        SELECT questions_answer.id AS "answer_id", 
               questions_answer.question_id, 
               questions_answer.user_id, 
               questions_answer.answer_text, 
               questions_answer.created_at, 
               questions_answer.sub_question
        FROM questions_answer
        """
    if table == "consent":
        return """
        SELECT questions_consent.id AS "consent_id", 
               questions_consent.user_id, 
               questions_consent.consent_given, 
               questions_consent.timestamp
        FROM questions_consent
        """
    if table == "profiles":
        return """
        SELECT profiles_profile.id AS "profile_id", 
               profiles_profile.user_id, 
               profiles_profile.bio, 
               profiles_profile.avatar, 
               profiles_profile.slug,
               profiles_profile.condition_id
        FROM profiles_profile
        """
    if table == "configuration":
        return """
        SELECT configuration_configuration.id AS "config_id", 
               configuration_configuration.like_dislike_enabled, 
               configuration_configuration.registration_enabled, 
               configuration_configuration.management_token, 
               configuration_configuration.is_timer_enabled, 
               configuration_configuration.max_session_duration
        FROM configuration_configuration
        """
    if table == "django_admin_log":
        return """
        SELECT django_admin_log.id AS "log_id", 
               django_admin_log.action_time, 
               django_admin_log.user_id, 
               django_admin_log.content_type_id, 
               django_admin_log.object_id, 
               django_admin_log.object_repr, 
               django_admin_log.action_flag, 
               django_admin_log.change_message
        FROM django_admin_log
        """
    if table == "auth_permission":
        return """
        SELECT auth_permission.id AS "permission_id", 
               auth_permission.name, 
               auth_permission.content_type_id, 
               auth_permission.codename
        FROM auth_permission
        """
    if table == "auth_group":
        return """
        SELECT auth_group.id AS "group_id", 
               auth_group.name
        FROM auth_group
        """
    if table == "django_session":
        return """
        SELECT django_session.session_key, 
               django_session.session_data, 
               django_session.expire_date
        FROM django_session
        """
    return None
