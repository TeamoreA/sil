"""
Django settings for sil project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    # local apps
    "customers",
    "orders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "sil.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "sil.wsgi.application"

# configure application environments

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

DEBUG = env.bool("DEBUG", default=False)
TEMPLATE_DEBUG = DEBUG
SECRET_KEY = env.str("SECRET_KEY", "defaultkey")

# setting up postgress database
DATABASES = {"default": env.db()}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"

AUTH_USER_MODEL = "customers.Customer"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "oidc_auth.authentication.JSONWebTokenAuthentication",
        "oidc_auth.authentication.BearerTokenAuthentication",
    ),
}

OIDC_AUTH = {
    # Specify OpenID Connect endpoint. Configuration will be
    # automatically done based on the discovery document found
    # at <endpoint>/.well-known/openid-configuration
    "OIDC_ENDPOINT": "https://accounts.google.com",
    # Accepted audiences the ID Tokens can be issued to
    "OIDC_AUDIENCES": (
        "myapp",
        "customers",
    ),
    # (Optional) Function that resolves id_token into user.
    # This function receives a request and an id_token dict and expects to
    # return a User object. The default implementation tries to find the user
    # based on username (natural key) taken from the 'sub'-claim of the
    # id_token.
    "OIDC_RESOLVE_USER_FUNCTION": "oidc_auth.authentication.get_user_by_id",
    # (Optional) Number of seconds in the past valid tokens can be
    # issued (default 600)
    "OIDC_LEEWAY": 600,
    # (Optional) Time before signing keys will be refreshed (default 24 hrs)
    "OIDC_JWKS_EXPIRATION_TIME": 24 * 60 * 60,
    # (Optional) Time before bearer token validity is verified again
    "OIDC_BEARER_TOKEN_EXPIRATION_TIME": 10 * 60,
    # (Optional) Token prefix in JWT authorization header (default 'JWT')
    "JWT_AUTH_HEADER_PREFIX": "JWT",
    # (Optional) Token prefix in Bearer authorization header (default 'Bearer')
    "BEARER_AUTH_HEADER_PREFIX": "Bearer",
    # (Optional) Which Django cache to use
    "OIDC_CACHE_NAME": "default",
    # (Optional) A cache key prefix when storing and retrieving cached values
    "OIDC_CACHE_PREFIX": "oidc_auth.",
}
