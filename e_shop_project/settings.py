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

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_!ef+fs_esvh64&&ul817030iqh0d)6ox#84f&mp!mcqy)5qxk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #internal app
    'accounte_module',
    'product_module',
    'contact_module',
    'site_module',
    'cart_module',
    'admin_panel',
    #extrnal app
    'rest_framework',
    'rest_framework_simplejwt', #JWT ui setting
    'drf_spectacular', #swagger ui setting
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'e_shop_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'e_shop_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

AUTH_USER_MODEL = 'accounte_module.User'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'fa-ir'#'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root/')

MEDIA_ROOT = BASE_DIR / 'uploads'
MEDIA_URL = '/medias/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#email setting
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'testingmyworksdjango@gmail.com'
# EMAIL_HOST_PASSWORD = 'cqisokqvcekoyhzl'
# EMAIL_PORT = 587 # when we use gmail, we must use port 587!
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False




REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],

     'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema', #swagger ui setting

# thorttling برای کنترل درخواست هاس تعداد و زمان
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.ScopedRateThrottle',
    ],
#این بخش برای زمان و تعداد درخواست ها = (request)
    'DEFAULT_THROTTLE_RATES': {
        'anon': '40/hour',
        'user': '50/hour',
        'get_request': '90/hour',
    }
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'e_shop_project',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
}




#/تنظیمات JWT/ در اینجا ما به تمام قسمت ها دسترسی داریم!
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=25),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": settings.SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

# "refresh":
# "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NjA3ODAzNSwiaWF0IjoxNjgzOTE4MDM1LCJqdGkiOiJjN2ZhY2VjYTM3OWE0NDAzYjcyYmVjZmQ2N2E3ZjJhMSIsInVzZXJfaWQiOjE4fQ.9OIxiPJWLiSlvhdhIZQy-B6plgAn4Gw9lOLS8gSeWOI",

# "access":
# "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg1MjE0MDM1LCJpYXQiOjE2ODM5MTgwMzUsImp0aSI6IjRmZjc5OGI3OWU0YjQyNGU4ZGQ4YjQwNWQ5N2UxZWM2IiwidXNlcl9pZCI6MTh9.IcEm0GU-9iSIL1XNx66Ci8gf1qzWoJke5_udRaGWfc8"

# decorator login required (redirect)
LOGIN_URL = 'http://127.0.0.1:8000/account/user-login/'