#!/usr/bin/env bash
set -e

# Корень репозитория (откуда запускается Railpack)
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

echo "==> Installing Python dependencies..."
pip install -r back/kids_project/requirements.txt

echo "==> Running migrations..."
cd back/kids_project
python manage.py migrate --noinput
cd "$ROOT"

echo "==> Building frontend..."
cd pr
npm ci
npm run build
cd "$ROOT"

echo "==> Starting application..."
cd back/kids_project
export PORT="${PORT:-8000}"
exec gunicorn kids_project.wsgi:application --bind "0.0.0.0:$PORT"
