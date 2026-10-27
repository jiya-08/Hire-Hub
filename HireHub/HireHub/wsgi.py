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
