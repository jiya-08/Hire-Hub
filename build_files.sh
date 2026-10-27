#!/bin/bash
set -e

echo "=== Installing Python dependencies ==="
if command -v uv &> /dev/null; then
    echo "Using uv to install dependencies..."
    uv pip install -r requirements.txt --system || python3 -m pip install -r requirements.txt --break-system-packages
else
    echo "Using pip to install dependencies..."
    python3 -m pip install -r requirements.txt --break-system-packages
fi

echo "=== Collecting Static Files ==="
python3 HireHub/manage.py collectstatic --noinput --clear

echo "=== Running Database Migrations ==="
python3 HireHub/manage.py migrate --noinput || true

echo "=== Build Complete ==="
