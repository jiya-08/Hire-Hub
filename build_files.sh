#!/bin/bash
set -e

echo "=== Installing Python dependencies ==="
python3 -m pip install -r requirements.txt

echo "=== Collecting Static Files ==="
python3 HireHub/manage.py collectstatic --noinput --clear

echo "=== Running Database Migrations ==="
python3 HireHub/manage.py migrate --noinput || true

echo "=== Build Complete ==="
