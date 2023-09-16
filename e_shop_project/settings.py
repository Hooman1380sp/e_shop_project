"""
Django settings for e_shop_project project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os.path
from pathlib import Path
from django.conf import settings
from datetime import timedelta
import os
# from dotenv import load_dotenv
# from django.core.management.utils import get_random_secret_key

# load_dotenv()
# settings.configure()All
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# os.environ.setdefault("DJANGO_SETTING_MODULE","e_shop_project")
# settings.configure()
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-_!ef+fs_esvh64&&ul817030iqh0d)6ox#84f&mp!mcqy)5qxk"
#'django-insecure-_!ef+fs_esvh64&&ul817030iqh0d)6ox#84f&mp!mcqy)5qxk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

LOCAL_APPS = [
    "account_module",
    "product_module",
    "contact_module",
    "site_module",
    "cart_module",
    "admin_panel",
]

EXTERNAL_APPS = [
    "rest_framework",
    "rest_framework_simplejwt",  # JWT ui setting
    "drf_spectacular",  # swagger ui setting
    "corsheaders",
]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # internal app
    *LOCAL_APPS,
    # external app
    *EXTERNAL_APPS,
]
# Cors headers
CORS_ALLOWED_ORIGINS = [
    "https://Hoomansp80.pythonanywhere.com",
    "http://localhost:8000",
    "http://127.0.0.1:9000",
]
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)
CORS_ALLOW_CREDENTIALS = True

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # external middleware
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "e_shop_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "e_shop_project.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

AUTH_USER_MODEL = "account_module.User"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': "Hoomansp80$default",
#         'HOST': "Hoomansp80.mysql.pythonanywhere-services.com",
#         'USER': "Hoomansp80",
#         'PASSWORD': "pGH3BeA$ULYS$Va",
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "fa-ir"  # 'en-us'

TIME_ZONE = "UTC"
# TIME_ZONE = "Asia/Tehran"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

<<<<<<< HEAD
STATIC_URL = "static/"
=======
STATIC_URL = "/static/"
>>>>>>> b94daef51115a9b660a0ffd999e6f2c7641c3873
STATIC_ROOT = BASE_DIR / "statics/"
# STATICFILES_DIRS = [
#     BASE_DIR / 'statics'
# ]

MEDIA_ROOT = BASE_DIR / "uploads"
MEDIA_URL = "/medias/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",  # swagger ui setting

    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
        "rest_framework.throttling.ScopedRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": "20/hour",
        "user": "30/hour",
        "get_request": "25/hour",
    },
}

SPECTACULAR_SETTINGS = {
    "TITLE": "e shop project",
    "DESCRIPTION": "shop project is recently version and big refactor!!",
    "VERSION": "1.0.0",
    # "SERVE_INCLUDE_SCHEMA": False,
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=2),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=40),
}

# LOGIN_URL = "/account/user-login/"
