
mkdir media staticfiles static

python manage.py makemigrations 
python manage.py migrate 
python manage.py collectstatic --noinput


DJANGO_SUPERUSER_USERNAME=andru \
DJANGO_SUPERUSER_PASSWORD=1234 \
DJANGO_SUPERUSER_EMAIL="andru.ocatorres@gmail.com" \
python manage.py createsuperuser --noinput

gunicorn products_api.wsgi:application --bind "0.0.0.0:8000"