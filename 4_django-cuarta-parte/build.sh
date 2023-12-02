#!/usr/bin/env bash

set -o errexit  # exit on error

pip install -r requirements.txt

mkdir  staticfiles media
python manage.py collectstatic -link --no-input
python manage.py makemigrations
python manage.py migrate

DJANGO_SUPERUSER_USERNAME=andru \
DJANGO_SUPERUSER_PASSWORD=1234 \
DJANGO_SUPERUSER_EMAIL="andru@mail.com" \
python manage.py createsuperuser --noinput
