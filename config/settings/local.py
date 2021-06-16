from datetime import timedelta

from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="UbKJh4hWKVtujX3OGSbtoHK5pb4O1f5TW8JzntNDnEhHyss8i2QKdCc6weM3b7C6",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["example.com"])
# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}
# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = "admin/"
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = env.list("ADMINS_LIST")
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)
# configure the sending email

EMAIL_HOST = env(
    "EMAIL_HOST"
)
EMAIL_HOST_USER = env(
    "EMAIL_HOST_USER"
)
EMAIL_HOST_PASSWORD = env(
    "EMAIL_HOST_PASSWORD"
)
EMAIL_PORT = env.int(
    "EMAIL_PORT"
)
EMAIL_USE_TLS = env.bool(
    "EMAIL_USE_TLS",
    default=True
)
DEFAULT_FROM_EMAIL = env(
    "DEFAULT_FROM_EMAIL"
)
DEFAULT_CONTACT_EMAIL = env(
    "DEFAULT_CONTACT_EMAIL"
)

EMAIL_TIMEOUT = env.int(
    "DJANGO_EMAIL_BACKEND", default=5
)
# WhiteNoise
# ------------------------------------------------------------------------------
# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS  # noqa F405

# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ["django_extensions"]  # noqa F405

#rest_framework_simplejwt
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'uuid',
    'USER_ID_CLAIM': 'user_uuid',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# Django REST Framework

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
    'rest_framework.renderers.JSONRenderer',
    'rest_framework.renderers.MultiPartRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.AllowAny",
        "rest_framework.permissions.IsAuthenticated",
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 2,

}

# django-cors-headers
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=["localhost"])

CORS_ORIGIN_WHITELIST = env.list("CORS_ORIGIN_WHITELIST ", default=["localhost"])

CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=["localhost"])

# url for token
URL_TOKE_SEND_ACCOUNT = env("URL_TOKE_SEND_ACCOUNT", default="localhost")
URL_TOKE_SEND_RESET_PASSWORD = env("URL_TOKE_SEND_RESET_PASSWORD", default="localhost")
