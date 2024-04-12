from pathlib import Path
from datetime import timedelta
from decouple import config
import datetime
import os

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-t6v+i#j5vrv8u*q(-a$k$u0l5d9$3n^sb*!^*9o6=o)l^l)1*g'

DEBUG = False

ALLOWED_HOSTS = ['mirbeko.pythonanywhere.com']


INSTALLED_APPS = [
    'django.contrib.staticfiles',   # +++
    'whitenoise.runserver_nostatic',    # +++
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    # 3 th packages
    'rest_framework',
    # 'rest_framework_simplejwt.token_blacklist',
    # 'django_filters',
    # 'django_rest_passwordreset',
    'rest_framework_simplejwt.token_blacklist',
    'django_filters',
    # 'django_rest_passwordreset', 
    'drf_yasg',

    # apps
    'apps.accounts',
    'apps.appartments'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",    # +++
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

AUTH_USER_MODEL = 'accounts.CustomUser'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Bishkek'
USE_I18N = True
USE_TZ = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



if DEBUG:
    from .dev_settings import *

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')      # ++++
STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"  # ++++


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        "rest_framework.authentication.SessionAuthentication",
    ],
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

SIMPLE_JWT = {
     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
     'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
     'ROTATE_REFRESH_TOKENS': True,
     'BLACKLIST_AFTER_ROTATION': True
}

APPEND_SLASH = True
