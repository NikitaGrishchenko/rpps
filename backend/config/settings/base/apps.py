DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "import_export",
    "corsheaders",
    "widget_tweaks",
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "drf_yasg",
    "django_cleanup.apps.CleanupConfig",
    "webpack_loader",
    "constance",
    "constance.backends.database",
    "etc",
    "drf_multiple_model",
    # "rest_framework_simplejwt.token_blacklist",
    "django_extensions",
    "service_objects",
]

PROJECT_APPS = [
    "apps.core.utils",
    "apps.core.main",
    "apps.core.api",
    "apps.api.auth",
    "apps.api.questioning",
    "apps.api.reference",
    "apps.api.documents",
]

DEVELOPER_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
]

PRODUCTION_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
]

IMPORT_EXPORT_TRANSACTIONS = True
