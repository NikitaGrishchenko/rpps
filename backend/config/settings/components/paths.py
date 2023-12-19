"""Paths settings"""

import os

from config.settings.base import env

# Base
CONFIG_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
BACKEND_DIR = os.path.dirname(CONFIG_DIR)
PROJECT_DIR = os.path.dirname(BACKEND_DIR)
ENV_FILE = os.path.join(PROJECT_DIR, ".env")
ENV_FILE_EXAMPLE = os.path.join(PROJECT_DIR, ".env.example")

# Nginx
PUBLIC_DIR = os.path.join(PROJECT_DIR, "serve")
PUBLIC_MEDIA_DIR = os.path.join(PUBLIC_DIR, "media")
PUBLIC_STATIC_DIR = os.path.join(PUBLIC_DIR, "static")

# Backend
LOGS_DIR = os.path.join(PUBLIC_DIR, "logs")
KEYS_DIR = os.path.join(PUBLIC_DIR, "keys")
APPS_DIR = os.path.join(BACKEND_DIR, "apps")
FIXTURES_DIR = os.path.join(BACKEND_DIR, "fixtures")
# LOG_FILE = os.path.join(LOGS_DIR, "{time:DD-MM-YYYY}.log")
DEV_DATABASE_FILE = os.path.join(PUBLIC_DIR, "db.sqlite3")
TEST_DATABASE_FILE = os.path.join(PUBLIC_DIR, "test_db.sqlite3")
FIXTURE_DIRS = [
    FIXTURES_DIR,
]

# Apps templates
APP_TEMPLATES = os.path.join(APPS_DIR, "core", "utils", "app_templates")
API_APP_TEMPLATE = os.path.join(APP_TEMPLATES, "api.zip")
CORE_APP_TEMPLATE = os.path.join(APP_TEMPLATES, "core.zip")
DEFAULT_APP_TEMPLATE = os.path.join(APP_TEMPLATES, "default.zip")

# Frontend
FRONTEND_DIR = os.path.join(PROJECT_DIR, "frontend")
STATIC_DIR = os.path.join(FRONTEND_DIR, "static")
DIST_DIR = os.path.join(STATIC_DIR, "dist")
TEMPLATES_DIR = os.path.join(FRONTEND_DIR, "templates")
WEBPACK_STATS_FILE = os.path.join(DIST_DIR, "webpack-stats.json")

# Docker volumes
DOCKER_LOG_DIR = os.path.join(
    PROJECT_DIR, env("DOCKER_LOG_DIR", default=".docker/logs")
)
DOCKER_MEDIA_DIR = os.path.join(
    PROJECT_DIR, env("DOCKER_MEDIA_DIR", default=".docker/media")
)
DOCKER_STATIC_DIR = os.path.join(
    PROJECT_DIR, env("DOCKER_STATIC_DIR", default=".docker/static")
)
DOCKER_DB_DIR = os.path.join(
    PROJECT_DIR, env("DOCKER_DB_DIR", default=".docker/db")
)
