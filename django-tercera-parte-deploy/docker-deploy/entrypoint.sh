
python manage.py wait_for_db
python manage.py makemigrations 
python manage.py migrate 
python manage.py collectstatic --noinput


gunicorn vinoteca.wsgi:application --bind "0.0.0.0:8000"
