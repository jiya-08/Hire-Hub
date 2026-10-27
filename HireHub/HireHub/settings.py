import os
from pathlib import Path
import dj_database_url

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-#04yz$_%cn*fna*24@gt_cei$p3=#xblg=2ccu3)_8(py07r!y"
)

DEBUG = os.environ.get("DEBUG", "True").lower() in ("true", "1")

ALLOWED_HOSTS = ["*", ".vercel.app", "localhost", "127.0.0.1"]


INSTALLED_APPS = [
    "jazzmin",

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "usersapp",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "HireHub.urls"


# ============================
# Templates
# ============================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "HireHub.wsgi.application"


# ============================
# Database Configuration
# ============================

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
else:
    # On Vercel serverless functions, the root is read-only; /tmp is writable
    if "VERCEL" in os.environ:
        db_path = Path("/tmp") / "db.sqlite3"
    else:
        db_path = BASE_DIR / "db.sqlite3"

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": db_path,
        }
    }


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


# ============================
# Internationalization
# ============================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


# ============================
# Static & Media Files
# ============================

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR.parent / "staticfiles_build" / "static"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# ============================
# Default Primary Key
# ============================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ============================
# Jazzmin Settings
# ============================

JAZZMIN_SETTINGS = {

    "site_title": "HireHub Admin",

    "site_header": "HireHub",

    "site_brand": "HireHub",

    "welcome_sign": "Welcome to HireHub Administration",

    "copyright": "HireHub 2026",

    "site_logo": None,

    "site_icon": None,

    "search_model": "usersapp.User",

    "show_sidebar": True,

    "navigation_expanded": True,

    "hide_apps": [],

    "hide_models": [],

    "related_modal_active": True,

    "changeform_format": "horizontal_tabs",

    "show_ui_builder": True,

    "icons": {
        "usersapp.User": "fas fa-user",
        "usersapp.Country": "fas fa-globe",
        "usersapp.State": "fas fa-map",
        "usersapp.City": "fas fa-city",
        "usersapp.FreelancerProfile": "fas fa-user-tie",
        "usersapp.JobCategory": "fas fa-list",
        "usersapp.Project": "fas fa-briefcase",
        "usersapp.Proposal": "fas fa-file-signature",
        "usersapp.Hire": "fas fa-handshake",
        "usersapp.Message": "fas fa-envelope",
        "usersapp.ContactUs": "fas fa-phone",
    },
}


# ============================
# Jazzmin UI Tweaks
# ============================

JAZZMIN_UI_TWEAKS = {

    "theme": "flatly",

    "dark_mode_theme": "darkly",

    "navbar": "navbar-dark navbar-primary",

    "sidebar": "sidebar-dark-primary",

    "accent": "accent-primary",

    "navbar_small_text": False,

    "sidebar_nav_small_text": False,

    "sidebar_disable_expand": False,

    "sidebar_nav_child_indent": True,

    "sidebar_nav_compact_style": False,

    "sidebar_nav_legacy_style": False,

    "actions_sticky_top": True,
}
