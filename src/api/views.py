import datetime
import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.db import transaction

# from advertisements.models import Advertisement
from api.forms import APIProfileModelForm, APIArticleModelForm
from configuration.models import get_the_config
# from posts.models import Post, PlannedReaction
from articles.models import Article
from comments.models import Comment
from profiles.models import Profile

from profiles.models import Profile

from django.contrib.auth.models import User


@csrf_exempt
def create_delete_comment(request):
    if request.method == "POST":
        return handle_create_comment(request)
    elif request.method == "DELETE":
        return handle_delete_comment(request)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


def handle_create_comment(request):
    # Extrahiere Daten aus den Query-Parametern
    profile_id = request.GET.get("profile_id")
    article_id = request.GET.get("article_id")
    content = request.GET.get("content")
    parent_comment_id = request.GET.get("parent_comment_id")

    # Überprüfe, ob alle erforderlichen Felder vorhanden sind
    if not all([profile_id, article_id, content]):
        return JsonResponse({"error": "Missing required fields: profile_id, article_id, content"}, status=400)

    try:
        # Hole die Profile- und Artikel-Objekte
        profile = get_object_or_404(Profile, id=profile_id)
        article = get_object_or_404(Article, id=article_id)
        # Optional: Hole den übergeordneten Kommentar
        parent_comment = Comment.objects.filter(id=parent_comment_id).first() if parent_comment_id else None
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=404)

    # Erstelle einen neuen Kommentar
    comment = Comment.objects.create(
        author=profile,
        article=article,
        content=content,
        parent_comment=parent_comment,
    )
    return JsonResponse({"message": "Comment created successfully", "comment_id": comment.id}, status=201)


def handle_delete_comment(request):
    # Extrahiere die Kommentar-ID aus den Query-Parametern
    comment_id = request.GET.get("comment_id")
    if not comment_id:
        return JsonResponse({"error": "Missing comment_id"}, status=400)

    try:
        # Versuche den Kommentar zu löschen
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return JsonResponse({"message": "Comment deleted successfully"}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=404)
    
    
@csrf_exempt
def create_delete_article(request):
    # Allow only POST and DELETE methods
    if request.method != "POST" and request.method != "DELETE":
        return HttpResponse(content="405 Method Not Allowed", status=405)

    if request.method == "POST":
        # Retrieve parameters from request.POST
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()
        news_paper_id = request.POST.get("news_paper_id", "").strip()

        # Check if mandatory parameters are provided
        if not title or not content or not news_paper_id:
            return HttpResponse(content="400 - title, content, and news_paper_id are mandatory", status=400)

        try:
            # Convert `news_paper_id` to integer
            news_paper_id = int(news_paper_id)
        except ValueError:
            return HttpResponse(content="400 - news_paper_id must be an integer", status=400)

        # Check if an image is uploaded
        if not request.FILES.get("image"):
            return HttpResponse(content="400 - image is mandatory", status=400)

        form = APIArticleModelForm(request.POST, request.FILES)
        if not form.is_valid():
            return HttpResponse(content="400 Bad request - form is invalid", status=400)

        # Create and save the article
        article = form.save(commit=False)
        article.title = title
        article.content = content
        article.news_paper_id = news_paper_id
        article.image = request.FILES["image"]
        article.save()

        article_id = article.id

        print(f"[API] Created article {article_id}")

        return json_response({
            "articleId": article_id
        })

    elif request.method == "DELETE":
        # Retrieve `articleId` from request.GET
        try:
            article_id = int(request.GET.get("articleId", "").strip())
        except ValueError:
            return HttpResponse(content="400 - articleId must be integer", status=400)

        article = Article.objects.filter(id=article_id).first()

        if article is None:
            return HttpResponse(content="404 Not Found", status=404)

        article.delete()
        print(f"[API] Deleted article {article_id}")
        return HttpResponse(status=200)


@csrf_exempt
def create_user(request):
    if request.method != "POST":
        return HttpResponse(content="405 Method Not Allowed", status=405)

    # Daten aus der Anfrage abrufen
    username = request.GET.get("username", "").strip()
    password = request.GET.get("password", "").strip()
    email = request.GET.get("email", "").strip()
    bio = request.GET.get("bio", "").strip()
    condition_id = request.GET.get("condition_id", None)  # Condition ID abrufen


    if username == "" or password == "" or email == "":
        return HttpResponse(content="400 Bad request - Missing username, password, or email", status=400)

    # Überprüfen, ob Benutzername oder E-Mail bereits existieren
    if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
        return HttpResponse(content="409 Conflict - Username or email already in use", status=409)

    try:
        with transaction.atomic():  # Nutze eine Transaktion für konsistente Daten
            # Benutzer erstellen
            user = User.objects.create_user(username=username, email=email, password=password)

            # Profil automatisch durch Signal erstellt, hier Profil anpassen
            profile = Profile.objects.filter(user=user).first()

            # Falls eine Bio übergeben wurde, hinzufügen
            if bio:
                profile.bio = bio
            
            # condition id
            if condition_id is not None:
                try:
                    profile.condition_id = int(condition_id)  # Konvertiere in Integer
                except ValueError:
                    return HttpResponse(content="400 Bad request - Invalid condition_id", status=400)

            # Avatar hochladen, falls übergeben
            if request.FILES.get("avatar", None) is not None:
                form = APIProfileModelForm(request.POST, request.FILES)
                if not form.is_valid():
                    return HttpResponse(content="400 Bad request - Invalid avatar form", status=400)
                temp_profile = form.save(commit=False)
                profile.avatar = temp_profile.avatar

            # Profil speichern
            profile.save()

            print(f"[API] Created user {username}")

            return JsonResponse({
                "userId": user.id,
                "profileId": profile.id,
            })

    except Exception as e:
        print(f"Error creating user: {str(e)}")
        return HttpResponse(content="500 Internal Server Error", status=500)


def json_response(data):
    return HttpResponse(content=json.dumps(data), content_type="application/json", status=200)

def verify_token(request):
    return request.headers.get("Token", "") == get_the_config().management_token

