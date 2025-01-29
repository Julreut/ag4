"""
Django settings for fakebook project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import shutil
from dotenv import load_dotenv

load_dotenv()  # Liest die .env-Datei ein


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(f"Base dir: {BASE_DIR}")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n*vms&0n)98o4py0vpydyu1l3-qt2%g*hm8c5n31fg+)8bh@zy'

# SECURITY WARNING: don't run with debug turned on in production! ##aenderungJuliane
# DEBUG_MODE = False

# DEBUG = False
DEBUG = os.getenv('DEBUG_MODE', 'False').lower() == 'true'

# if DEBUG:
#     print("Enabling debug mode")

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0", "*"]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # 'django_extensions',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'profiles',

    'comments',
    'articles',
    'questions',

    'analytics',

    'configuration',
    'api',
]

SITE_ID = 1

#LOGIN_URL = '/admin/'
LOGIN_REDIRECT_URL = '/questions/redirect_to_questions/'
LOGOUT_REDIRECT_URL = '/questions/end/'

ACCOUNT_FORMS = {
    'signup': 'fakebook.forms.CustomSignupForm',  # Passe `your_app` an den Namen deiner App an
}
ACCOUNT_AUTHENTICATION_METHOD = "username"  # Nur Username für Authentifizierung
ACCOUNT_EMAIL_REQUIRED = False  # Email wird nicht benötigt
ACCOUNT_USERNAME_REQUIRED = True  # Username bleibt Pflichtfeld
# ACCOUNT_EMAIL_VERIFICATION = "optional"  # Email-Verifikation deaktivieren

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'fakebook.middleware.NewspaperTimerMiddleware',
]

# MAX_SESSION_DURATION = 3600  # 1 Stunde in Sekunden # not needed anymore

ROOT_URLCONF = 'fakebook.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'profiles.context_processors.profile_pic',
                'questions.context_processors.global_settings',
                'questions.context_processors.session_config'
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'fakebook.wsgi.application'
ASGI_APPLICATION = 'fakebook.asgi.application'


# Data directory
DATA_DIRECTORY = os.environ['DATA_DIRECTORY'] if 'DATA_DIRECTORY' in os.environ else "data"

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_DIRECTORY, 'db.sqlite3'),
    }
}

## URLS
APPEND_SLASH = True  # Standardmäßig aktiviert

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
        {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 2,  #mind 2 Zeichen
        },
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

# LOCALE_PATHS = [
#     os.path.join(BASE_DIR, "posts", "locale")
# ]


TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = (
    ('en', 'English'),
    ('de', 'Deutsch')
)

LANGUAGE_CODE = 'en'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_project/css'),
    os.path.join(BASE_DIR, 'static_project/js'),
]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "static_root")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIRECTORY, "media")



# # Settings - TODO: load from environment
# ANALYTICS_UPDATE_PERIOD_MS = 3000
# ANALYTICS_SESSION_TIMEOUT_MS = 30000

# in case it doesn't exist copy template db in data.template/ to data/
import shutil

def copy_db_template():
    template_db_path = "data.template/db.sqlite3"
    target_db_path = os.path.join(DATA_DIRECTORY, 'db.sqlite3')

    # Überprüfe, ob das Vorlagenverzeichnis existiert
    if not os.path.isdir("data.template"):
        print("Default database template not found, skipping creation...")
        return

    # Erstelle das DATA_DIRECTORY, falls es nicht existiert
    if not os.path.isdir(DATA_DIRECTORY):
        os.mkdir(DATA_DIRECTORY)

    # Kopiere die Datenbank nur, wenn sie noch nicht existiert
    if not os.path.isfile(target_db_path):
        print(f"Database not found at {target_db_path}. Copying template database...")
        shutil.copy(template_db_path, target_db_path)
        print("Template database copied successfully.")

        # Kopiere den Media-Ordner, falls er in der Vorlage existiert
        template_media_path = "data.template/media"
        target_media_path = os.path.join(DATA_DIRECTORY, "media")

        if os.path.isdir(template_media_path):
            if not os.path.isdir(target_media_path):
                shutil.copytree(template_media_path, target_media_path)
                print("Template media folder copied successfully.")
    else:
        print("Database already exists. Skipping template copy.")

