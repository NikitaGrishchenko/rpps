from config.settings.base import env

DEFAULT_MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


DEVELOPER_MIDDLEWARE = [
    *DEFAULT_MIDDLEWARE,
]

if env("USE_QUERYCOUNT", default=False):
    DEVELOPER_MIDDLEWARE.append("querycount.middleware.QueryCountMiddleware",)


PRODUCTION_MIDDLEWARE = [
    *DEFAULT_MIDDLEWARE,
]
