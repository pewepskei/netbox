#!/bin/bash
set -e

echo "Running NetBox migrations..."
python manage.py migrate --no-input

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Starting NetBox..."
exec gunicorn \
  --bind 0.0.0.0:8080 \
  --workers ${GUNICORN_WORKERS:-3} \
  --timeout ${GUNICORN_TIMEOUT:-120} \
  netbox.wsgi
