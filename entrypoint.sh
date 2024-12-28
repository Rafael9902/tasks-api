#!/bin/bash
set -e

echo "Running database migrations..."
poetry run python manage.py makemigrations
poetry run python manage.py migrate

exec "$@"
