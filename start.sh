#!/usr/bin/env bash
set -e

# Корень репозитория (откуда запускается Railpack)
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

# Python: на Railway часто только python3 в PATH
if command -v python3 &>/dev/null; then
  PY=python3
elif command -v python &>/dev/null; then
  PY=python
else
  echo "ERROR: Neither python nor python3 found in PATH." && exit 1
fi

echo "==> Installing Python dependencies (using $PY)..."
"$PY" -m pip install -r back/kids_project/requirements.txt

echo "==> Running migrations..."
cd back/kids_project
"$PY" manage.py migrate --noinput
cd "$ROOT"

echo "==> Building frontend..."
cd pr
npm install
npm run build
cd "$ROOT"

echo "==> Starting application..."
cd back/kids_project
export PORT="${PORT:-8000}"
exec "$PY" -m gunicorn kids_project.wsgi:application --bind "0.0.0.0:$PORT"
