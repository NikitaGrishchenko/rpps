"""Rest framework settings"""
from datetime import timedelta

from config.settings.base import env

REST_FRAMEWORK = {
    "DATETIME_INPUT_FORMATS": ["%d.%m.%Y, %H:%M",],
    "DATETIME_FORMAT": "%d.%m.%Y %H:%M",
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ),
    "DEFAULT_RENDERER_CLASSES": (
        "djangorestframework_camel_case.render.CamelCaseJSONRenderer",
        "djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer",
    ),
    "DEFAULT_PARSER_CLASSES": (
        "djangorestframework_camel_case.parser.CamelCaseFormParser",
        "djangorestframework_camel_case.parser.CamelCaseMultiPartParser",
        "djangorestframework_camel_case.parser.CamelCaseJSONParser",
    ),
}

# включить в dj_rest_auth поддержку jwt
REST_USE_JWT = True

# наименование токена
JWT_AUTH_COOKIE = "access_token"

# Список источников, которым разрешено делать межсайтовые HTTP-запросы
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
]

# Если True файлы cookie будут
# разрешены для включения в межсайтовые HTTP-запросы
CORS_ALLOW_CREDENTIALS = True

# настройка drf-simplejwt на базе которого написан dj_rest_auth
SIMPLE_JWT = {
    # "ACCESS_TOKEN_LIFETIME": timedelta(minutes=1440),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=144000),
    "AUTH_COOKIE_SECURE": True,
    "AUTH_COOKIE_SAMESITE": "Strict",
}
