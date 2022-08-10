web: gunicorn GenBackend.wsgi
release: python manage.py makemigrations && python manage.py migrate --noinput
release: python manage.py collectstatic --noinput
release: python manage.py createsuperuser