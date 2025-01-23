from fakebook.downloads import get_xlsx_file_from_database, get_database, get_zip_file
from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from configuration.models import get_the_config

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages

from profiles.models import Profile

from django.http import HttpResponseNotFound


import json

def home_view(request):
    user = request.user
    hello = 'Hello World'

    context = {
        'user': user,
        'hello': hello,
    }

    # return render(request, 'main/home.html', context)
    return redirect('questions:experiment_start')

@user_passes_test(lambda u: u.is_superuser)
def user_creation_view(request):
    return render(request, 'admin/custom_create_user.html')

@user_passes_test(lambda u: u.is_superuser)
def create_user(request):
    if request.method != "POST":
        return HttpResponse(content="405 Method Not Allowed", status=405)

    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    bio = request.POST.get("bio", "")

    if username == "" or password == "":
        # shouldn't happen, UI will require input, so it's fine to just return 400
        return HttpResponse(content="400 Bad request", status=400)

    if User.objects.filter(username=username).exists():
        messages.add_message(request, messages.ERROR, "Conflict detected - username already in use. No action was taken.")
        # return HttpResponse(content="409 Conflict - username or email already in use", status=409)
        return redirect('user-creation-view')


    user = User.objects.create_user(username=username, password=password)
    # profile is automatically created by signal
    profile = Profile.objects.filter(user=user).first()

    if bio != "":
        profile.bio = bio

    # for profile image support, use API route
    # This is not supported here as the view is not a form and would therefore have to manually implement uploading images

    user.save()
    profile.save()

    messages.add_message(request, messages.SUCCESS, f"User with username {user.username}, id {user.id} and profile {profile.id} created successfully!")

    return redirect('user-creation-view')

@user_passes_test(lambda u: u.is_superuser)
def download_view(request):
    return render(request, 'admin/download_database.html')

@user_passes_test(lambda u: u.is_superuser)
def download_xlsx(request):
    # Tabellen, die verfügbar sind
    tables = [
        "user", "comments", "likes", "dislikes", 
        "articles", "newspapers", "usereventlog", 
        "usercontentposition", "experimentcondition"
    ]
    selected_tables = []

    # Überprüfen, welche Tabellen ausgewählt wurden
    for entry in tables:
        if str(request.POST.get(entry)) == "on":
            selected_tables.append(entry)

    # XLSX-Datei generieren
    xlsx_file = get_xlsx_file_from_database(selected_tables)
    return xlsx_file

@user_passes_test(lambda u: u.is_superuser)
def download_database(request):
    database = get_database()
    return database

@user_passes_test(lambda u: u.is_superuser)
def download_pictures(request):
    # Definiere verfügbare Archive
    archives = ["articles", "newspapers", "profile_pictures"]
    selected_archives = []

    # Überprüfen, welche Archive ausgewählt wurden
    for entry in archives:
        if str(request.POST.get(entry)) == "on":
            selected_archives.append(entry)

    # ZIP-Datei generieren
    zip_file = get_zip_file(selected_archives)
    return zip_file


@csrf_exempt
def is_registration_enabled(request):
    return json_response({
        "registration_enabled": get_the_config().registration_enabled
    })

def json_response(data):
    return HttpResponse(content=json.dumps(data), content_type="application/json", status=200)


def placeholder_view(request):
    return HttpResponseNotFound("This endpoint is not implemented.")