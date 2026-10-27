"""
WSGI config for HireHub project on Vercel and local environments.

It exposes the WSGI callable as a module-level variable named ``application``
and ``app`` (required by Vercel Serverless Functions).
"""

import os
import sys
from pathlib import Path

# Add project root directory to sys.path so inner modules can be imported
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = CURRENT_DIR.parent
ROOT_DIR = PROJECT_DIR.parent

for directory in (str(PROJECT_DIR), str(ROOT_DIR)):
    if directory not in sys.path:
        sys.path.insert(0, directory)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HireHub.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
app = application


# Auto-initialize database tables and default admin user on serverless environments
def init_serverless_db():
    try:
        from django.core.management import call_command
        from django.contrib.auth import get_user_model
        from django.db import connection

        tables = connection.introspection.table_names()
        if "django_session" not in tables:
            call_command("migrate", interactive=False)

        User = get_user_model()
        admin_user = os.environ.get("ADMIN_USERNAME", "admin")
        admin_password = os.environ.get("ADMIN_PASSWORD", "admin123")
        admin_email = os.environ.get("ADMIN_EMAIL", "admin@hirehub.com")

        if not User.objects.filter(username=admin_user).exists():
            User.objects.create_superuser(admin_user, admin_email, admin_password)
            print(f"Serverless superuser '{admin_user}' initialized.")
    except Exception as exc:
        print(f"Serverless DB init note: {exc}")


init_serverless_db()
